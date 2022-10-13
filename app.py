from flask import Flask

app = Flask(__name__)


@app.route('/send_to_bot', methods=['POST', 'GET'])
def send_to_bot(message):
    """

    :return:
    """
    return True


if __name__ == "__main__":
    app.run(debug=True, port=80)
