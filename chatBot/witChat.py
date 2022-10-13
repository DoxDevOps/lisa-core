from pywit.wit import Wit
from config.config import config

_access_token_ = config["_access_token_"]
client = Wit(_access_token_)


def get_intent_from_wit(message_to_wit):
    entity = {}
    response = client.message(message_to_wit)

    try:
        entity = list(response['entities'])

        return entity
    except:
        pass
    return entity



