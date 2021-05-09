from flask import Flask

app = Flask(__name__, static_url_path="") # flask object

@app.route("/test")
def test_flask() -> str:
    """
    simply for test
    :return: str
    """
    return "<h1>TEST PAGE</h1>"

@app.route("/auth")
def authenticate() -> str:
    """
    simply for test
    :return: str
    """
    return "<h1>TEST PAGE</h1>"

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
    app.run(host="0.0.0.0", port=80, debug=False)