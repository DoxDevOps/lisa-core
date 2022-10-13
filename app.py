from flask import Flask

from chatBot.witChat import get_intent_from_wit

app = Flask(__name__)


@app.route('/send_to_bot', methods=['POST', 'GET'])
def send_to_bot(message):
    """
    gets a message and sends it to Bot

    :return:
    """
    entities = get_intent_from_wit(message)
    return entities


if __name__ == "__main__":
    app.run(debug=True, port=80)
