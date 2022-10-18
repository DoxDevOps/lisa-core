# Modules
import random
from config.config import config
from utils.botResponse import intent_response


# from utils.databaseOperations import check_last_conversation, check_if_number_exist, save_conversation

# *********Config*******************
token = config["token"]
response_message: str = config["response_message"]
facebook_url = config["facebook_url"]
helpdesk_url = config["helpdesk_url"]

# ********* Intents ************
bot_null_response = intent_response["null"]
bot_greeting_response = intent_response["greeting:greeting"]
bot_greeting_log_intent = intent_response[
    "greeting:greeting,intent_log_ticket:intent_log_ticket"
]
bot_greeting_check_intent = intent_response[
    "greeting:greeting,intent_check_ticket:intent_check_ticket"
]
bot_greeting_intent_log_ticket = intent_response[
    "greeting:greeting,intent_log_ticket:intent_log_ticket,log_ticket:log_ticket"
]
bot_greeting_intent_check_ticket = intent_response[
    "greeting:greeting,intent_check_ticket:intention_check_ticket,"
    "check_ticket:check_ticket"
]
bot_greeting_log_ticket = ["greeting:greeting,log_ticket:log_ticket"]
bot_greeting_check_ticket = ["intent_log_ticket:intent_log_ticket,log_ticket:log_ticket"]
bot_intent_log_ticket = ["intent_log_ticket:intent_log_ticket,log_ticket:log_ticket"]
bot_intent_check_ticket = ["intent_check_ticket:intent_check_ticket"]
bot_log_ticket = ["log_ticket:log_ticket"]
bot_check_ticket = ["check_ticket:check_ticket"]

# expected intents
# for new intents, simple add them to this dict and everything will still hold
expected_intents = {
    1: {
        "intent": ["greeting:greeting"],
        "response": "greeting:greeting",
    },
    2: {
        "intent": ["intent_log_ticket:intent_log_ticket"],
        "response": "intent_log_ticket:intent_log_ticket",
    },
    3: {
        "intent": ["log_ticket:log_ticket"],
        "response": "log_ticket:log_ticket",
    },
    4: {
        "intent": ["intent_check_ticket:intent_check_ticket"],
        "response": ["intent_check_ticket:intent_check_ticket"]
    },
    5: {
        "intent": ["check_ticket:check_ticket"],
        "response": ["check_ticket:check_ticket"]
    }
}


def respond_to_intent(
    intents_from_nlp_engine: list[str],
    expected_intents: dict[int, dict],
    intent_response: dict[str, list],
) -> str:
    """responds to a user's intent

    Args:
        intents_from_nlp_engine (list[str]): intents from the NLP engine
        expected_intents (dict[int, dict]): intents that we are expecting to come in
        intent_response (dict[str, list]): possible responses

    Returns:
        str: response choosen randomly
    """

    responses = []

    if not intents_from_nlp_engine:
        return random.choice(intent_response["null"])

    for intent_from_nlp_engine in intents_from_nlp_engine:
        for expected_intent in expected_intents:
            if intent_from_nlp_engine == expected_intent["intent"]:
                responses.append(expected_intent["response"])

    # turn responses to strings separated by commas
    # check if responses is not empty
    # if empty, return default response
    resp = ", ".join(responses) if responses else "null"

    return random.choice(intent_response[resp])
