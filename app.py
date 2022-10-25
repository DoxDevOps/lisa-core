"""
Authentication code taken from : https://prettyprinted.com
"""
import datetime
import logging
import os

from flask import Flask, jsonify, request, make_response

from chatBot.processWitIntents import respond_to_intent
from config.witIntents import expected_intents
from utils.botResponse import intent_response
from chatBot.witChat import get_intent_from_wit
from functools import wraps
import jwt
# from config.config import config
from dotenv import load_dotenv


load_dotenv()  # load .env file


secret_key = os.environ.get("secret_authentication_key")
auth_username = os.environ.get("auth_username")
auth_password = os.environ.get("auth_password")

app = Flask(__name__)


@app.route('/test')
def test():
    """
    Tests if the application is reachable or not
    :return: json message
    """
    return jsonify({"SUCCESS": "The Application is running !!"}), 200


def token_required(f):
    """
    Checks if a request has a token in it
    :param f:
    :return:
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # token = request.args.get('token')

        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]

        if not token:
            return jsonify({"message": "Token is missing!"}), 403

        try:
            data = jwt.decode(token, secret_key, algorithms=["HS256"])
            print(data)
        except Exception as e:
            logging.info(f"Authentication failed with exception: {e}")
            return jsonify({"message": "Token is incorrect"}), 403
        return f(*args, **kwargs)

    return decorated


@app.route("/send_to_bot")
@token_required
def send_to_bot():
    """
    gets a message and sends it to Bot

    :return:
    """
    message = request.args["message"]
    print(message)
    if not message:
        return False
    entities = get_intent_from_wit(message)  # get all intents from wit.ai
    response_from_wit = respond_to_intent(entities, expected_intents, intent_response)
    return response_from_wit


@app.route("/authenticate")
def authenticate_me():
    """
    A function that authenticates and validates a request made to the service
    :return:
    """
    auth = request.authorization
    if auth and auth.password == auth_password and auth.username == auth_username:
        token = jwt.encode(
            {
                "user": auth.username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            },
            secret_key,
        )
        return jsonify({"token": token})
    return make_response(
        "Could not verify", 401, {"www-Authenticate": 'Basic realm="Login Required"'}
    )


if __name__ == "__main__":
    app.run(debug=True, port=80)
