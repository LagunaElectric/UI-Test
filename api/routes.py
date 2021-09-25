from typing import Dict

from api import app


@app.route("/test_message", methods=["GET"])
def test_message() -> Dict:
    return {"message": "hello world"}