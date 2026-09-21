from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username == "venkatesh" and password == "12345":
        return jsonify({
            "status": "success",
            "message": "Login successful"
        }), 200

    return jsonify({
        "status": "failed",
        "message": "Invalid credentials"
    }), 401


if __name__ == "__main__":
    app.run()
