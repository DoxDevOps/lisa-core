"""
Authentication code taken from : https://prettyprinted.com
"""
import datetime


from flask import Flask, jsonify, request, make_response

from chatBot.witChat import get_intent_from_wit
from functools import wraps
import jwt
from config.config import config
secret_key = config["secret_authentication_key"]
app = Flask(__name__)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        #token = request.args.get('token')


        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            data = jwt.decode(token, secret_key)
        except:
            return jsonify({'message': 'Token is Incorrect'}), 403
        return f(*args, **kwargs)

    return decorated


@app.route('/send_to_bot')
@token_required
def send_to_bot( ):
    """
    gets a message and sends it to Bot

    :return:
    """
    message = request.args["message"]
    print(message)
    if not message:
        return False
    entities = get_intent_from_wit(message)
    return entities


@app.route('/authenticate')
def authenticate_me():
    """
    A function that authenticates and validates a request made to the service
    :return:
    """
    auth = request.authorization
    if auth and auth.password == "SAMPLE PASSWORD":
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, secret_key)
        return jsonify({'token':token})
    return make_response('Could not verify', 401, {'www-Authenticate': 'Basic realm="Login Required"'})


if __name__ == "__main__":
    app.run(debug=True, port=80)
