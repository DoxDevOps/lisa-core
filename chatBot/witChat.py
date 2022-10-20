import os

import requests


# from config.config import config
from dotenv import load_dotenv


load_dotenv()  # load .env file

access_token = os.environ.get("access_token")
wit_url = os.environ.get("wit_url")


def get_intent_from_wit(message_to_wit):
    """
    A function that sends a message to wit. and returns a list of intents
    :param message_to_wit:
    :return: entity
    """
    entity = {}
    # response = client.message(message_to_wit)
    response = requests.get(wit_url+message_to_wit, headers={"Authorization": access_token})

    try:
        response = response.json()
        entity = list(response['entities'])

        return entity
    except:
        pass
    # return jsonify({'result': response.json()})



