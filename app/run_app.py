from flask import Flask, jsonify, request

from schema import Schema, SchemaError

from common.db import DBActions
from common.hashing import validate

app = Flask(__name__, static_url_path="") # flask object

login_schema = Schema(
    {
        "username": str,
        "password": str
    }
)

@app.route("/test")
def test_flask() -> str:
    """
    simply for test
    :return: str
    """
    return "<h1>TEST PAGE</h1>"

@app.route("/auth", methods=["POST"])
def authenticate() -> str:
    """
    simply for test
    :return: str
    """
    return_dict = {"login": False, "error_msg": None}
    if request.is_json:
        try:

            data = request.get_json()
            login_schema.validate(data)

        except SchemaError:
            return_dict.update({"error_msg": "JSON schema not met"})
        else:
            with DBActions() as db:
                username, pw_hash = db.get(
                    stored_proc="get_user",
                    values=tuple([data["username"], None])
                )

            if not pw_hash:
                return_dict.update({"error_msg": f"Unkown user: {username}"})
            else:
                if not validate(data["password"], pw_hash):
                    return_dict.update({"error_msg": "incorrect password"})
                else:
                    return_dict.update({"login": True})
    else:
        return_dict.update({"error_msg": f"Args must be JSON not: {str(request)}"})

    return jsonify(return_dict)

@app.route("/get")
def get() -> str:
    """
    simply for test
    :return: str
    """
    return "<h1>TEST PAGE</h1>"

@app.route("/put")
def put() -> str:
    """
    simply for test
    :return: str
    """
    return "<h1>TEST PAGE</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)