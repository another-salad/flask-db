"""Main flask application"""

from re import search

from flask import Flask, jsonify, request

from flask_jwt_extended import create_access_token, jwt_required, JWTManager

from schema import Schema, SchemaError

from common import ERROR_KEY, GET_USER_PROC, SECRET_KEY, DEBUG, IP, PORT
from common.db import DBActions
from common.enums import ErrorCodes, HTTPStatusCodes
from common.hashing import validate_pw
from common.json_encoder import DecimalJsonEncoder


app = Flask(__name__, static_url_path="") # flask object
app.config["JWT_SECRET_KEY"] = SECRET_KEY
app.json_encoder = DecimalJsonEncoder
jwt = JWTManager(app)


def validate_input(schema, input_data):
    """
    JSON input validator

    Args:
        schema (Schema): The Schema object
        input_data (flask.request): The flask request object

    Returns:
        [tuple]: int (Enum error code), dict or None (on error)
    """
    error = None
    return_data = None
    if not input_data.is_json:
        error = ErrorCodes.TYPE
    else:
        try:

            data = request.get_json()
            schema.validate(data)

        except SchemaError:
            error = ErrorCodes.SCHEMA

    if not error:
        error = ErrorCodes.SUCCESS
        return_data = data

    return error, return_data


authenticate_schema = Schema({"username": str, "password": str})
@app.route("/auth", methods=["POST"])
def authenticate() -> tuple:
    """
    Authenticates the user

    :return tuple: (JSON string: JWT, Error code), HTTP error code
    """
    return_dict = {}
    status_code = HTTPStatusCodes.UNAUTHORIZED
    error_code, data = validate_input(authenticate_schema, request)
    if error_code == 0:
        with DBActions() as db:
            _, pw_hash = db.get(
                stored_proc=GET_USER_PROC,
                values=tuple([data["username"], None])
            )

        if not pw_hash:
            return_dict.update({ERROR_KEY: ErrorCodes.UNKNOWN_USER})
        else:
            if not validate_pw(data["password"], pw_hash):
                return_dict.update({ERROR_KEY: ErrorCodes.INCORRECT_PASSWORD})
            else:
                return_dict.update({ERROR_KEY: ErrorCodes.SUCCESS, "access_token": create_access_token(identity=data["username"])})
                status_code = HTTPStatusCodes.OK
    else:
        return_dict.update({ERROR_KEY: error_code})
        status_code = HTTPStatusCodes.BAD_REQUEST

    return jsonify(return_dict), status_code


db_schema = Schema({"proc": str, "args": list})
@app.route("/call", methods=["POST"])
@jwt_required()
def call() -> tuple:
    """
    Excepts set or get DB calls

    :param string proc: The name of the stored procedure being called
    :param list args: The args for the stored param (including out variables (if required))

    :return tuple: (JSON string: Query results, Error code), HTTP error code
    """
    res = None
    error_occurred = True
    status_code = HTTPStatusCodes.OK
    error_code, data = validate_input(db_schema, request)
    if error_code == 0:
        attr_call = search(r"(?P<attr>get|set)_", data["proc"])
        if (not attr_call) or (not hasattr(DBActions, attr_call.group("attr"))):
            error_code = ErrorCodes.ATTRIB_ERROR
        else:
            attr_call = attr_call.group("attr")
            with DBActions() as db:
                try:

                    res = getattr(db, attr_call)(stored_proc=data["proc"], values=tuple(data["args"]))
                    error_occurred = False

                except Exception: # pylint: disable=broad-except
                    error_code = ErrorCodes.VALUE_ERROR

    if error_occurred:
        status_code = HTTPStatusCodes.BAD_REQUEST

    return jsonify({"response": res, ERROR_KEY: error_code}), status_code


if __name__ == "__main__":
    app.run(host=IP, port=PORT, debug=DEBUG)
