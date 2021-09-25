from typing import Dict

from api import app


@app.route("/debug/test_message", methods=["GET"])
def test_message() -> Dict:
    return {"message": "hello world"}

@app.route("/debug/database_contents", methods=["GET"])
def debug_database_contents() -> Dict:
    # Get all database contents
    # jsonify
    return {}