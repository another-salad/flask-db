from flask import Flask, jsonify, request
from flask_jwt import JWT, jwt_required, current_identity

from schema import Schema, SchemaError

from common import ERROR_KEY, GET_USER_PROC
from common.db import DBActions
from common.error_enums import ErrorCodes
from common.hashing import validate_pw


app = Flask(__name__, static_url_path="") # flask object


def validate_input(schema, input_data):
    """

    Args:
        schema ([type]): [description]
        input_data ([type]): [description]

    Returns:
        [type]: [description]
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

@app.route("/test")
def test_flask() -> str:
    """
    simply for test
    :return: str
    """
    return "<h1>TEST PAGE</h1>"


authenticate_schema = Schema({"username": str, "password": str})
@app.route("/auth", methods=["POST"])
def authenticate() -> str:
    """
    Authenticates the user

    :return: JSON string
    """
    return_dict = {}
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
                return_dict.update({ERROR_KEY: ErrorCodes.SUCCESS})
    else:
        return_dict.update({ERROR_KEY: error_code})

    return jsonify(return_dict)


db_schema = Schema({"proc": str, "args": tuple})
@app.route("/get")
def get() -> str:
    """
    simply for test
    :return: str
    """
    return jsonify({"auth": ErrorCodes.SUCCESS})


@app.route("/put")
def put() -> str:
    """
    simply for test
    :return: str
    """
    return "<h1>TEST PAGE</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)