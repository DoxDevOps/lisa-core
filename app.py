import datetime

import jwt as jwt
from flask import Flask, jsonify, make_response, request

from chatBot.witChat import get_intent_from_wit
from functools import wraps

app = Flask(__name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token is missing!'}),403
        try:
            data = jwt.decode(token, "SECREST")
        except:
            return jsonify({'message': 'Token is Invalid'}), 403
        return f(*args, **kwargs)
    return decorated
@app.route('/send_to_bot', methods=['POST', 'GET'])
def send_to_bot(message):
    """
    gets a message and sends it to Bot

    :return:
    """
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
        token =jwt.encode({'user':auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)})
    return True


if __name__ == "__main__":
    app.run(debug=True, port=80)
