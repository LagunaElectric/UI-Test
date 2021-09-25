from flask import Flask


app = Flask(__name__)


@app.route("/test_message", methods=["GET"])
def test_message():
    return {"message": "hello world"}


if __name__ == "__main__":
    app.run(debug=True)
