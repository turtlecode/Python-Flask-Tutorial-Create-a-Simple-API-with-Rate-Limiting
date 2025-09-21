from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Initialize the limiter, using IP address as the identifier
limiter = Limiter(
    key_func=get_remote_address,  # limits based on user's IP
    app=app,
    default_limits=[]
)

@app.route("/data", methods=["GET"])
@limiter.limit("3 per hour")
def get_data():
    return jsonify({"message": "Success! Here is your data."})

if __name__ == "__main__":
    app.run(debug=True)
