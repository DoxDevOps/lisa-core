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
bot_greeting_log_ticket = "greeting:greeting,log_ticket:log_ticket"
bot_greeting_check_ticket = "intent_log_ticket:intent_log_ticket,log_ticket:log_ticket"
bot_intent_log_ticket = "intent_log_ticket:intent_log_ticket,log_ticket:log_ticket"
bot_intent_check_ticket = "intent_check_ticket:intent_check_ticket"
bot_log_ticket = "log_ticket:log_ticket"
bot_check_ticket = "check_ticket:check_ticket"

# expected intents
# for new intents, simple add them to this dict and everythin will still hold
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
        "intent": "[log_ticket:log_ticket]",
        "response": "log_ticket:log_ticket",
    },
}


def respond_to_intent(
    intents_from_nlp_engine: list[str],
    expected_intents: dict[int, dict],
    intent_response: dict[str, list],
) -> str:
    """responds to a user accordingly based on intent

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


# **** Database operations *************
# from utils.modules import conversation


def process_intents(entity):
    """
    A function responsible for sending and receiving WhatsApp messages
    :param entity:

    :return:
    """

    try:

        if entity == {}:
            message_to_sender = random.choice(
                bot_null_response
            )  # get a random response
            return message_to_sender
        else:

            # check if the user already started a conversation
            # check_conversation = check_last_conversation(phone_number)
            new_conversation = True  # check_if_number_exist(phone_number)
            # if user_id and not check_conversation:
            if new_conversation:
                # that means it is a new conversation
                if ["greeting:greeting"] == entity:
                    save_new_conversation = True  # send to the database

                    if save_new_conversation:
                        # send the user a response message
                        greetings_message_to_sender = random.choice(
                            bot_greeting_response
                        )  # get a random response
                        return greetings_message_to_sender

                if [
                    "greeting:greeting",
                    "intent_log_ticket:intent_log_ticket",
                ] == entity:
                    save_new_conversation = True  # send to the database
                    if save_new_conversation:
                        message_to_client = random.choice(bot_greeting_log_intent)
                        return message_to_client

                if [
                    "greeting:greeting",
                    "intent_check_ticket:intent_check_ticket",
                ] == entity:
                    save_new_conversation = True
                    if save_new_conversation:
                        message_to_client = random.choice(bot_greeting_check_intent)
                        return message_to_client
                if [
                    "greeting:greeting",
                    "intent_log_ticket:intent_log_ticket",
                    "log_ticket:log_ticket",
                ]:
                    save_new_conversation = True
                    if save_new_conversation:
                        message_to_client = random.choice(
                            bot_greeting_intent_log_ticket
                        )
                        return message_to_client

                if [
                    "greeting:greeting",
                    "intent_check_ticket:intention_check_ticket",
                    "check_ticket" ":check_ticket",
                ]:
                    save_new_conversation = True
                    if save_new_conversation:
                        message_to_client = random.choice(
                            bot_greeting_intent_check_ticket
                        )
                        return message_to_client
                if ["greeting:greeting", "log_ticket:log_ticket"]:
                    save_new_conversation = True
                    if save_new_conversation:
                        message_to_client = random.choice(bot_greeting_log_ticket)
                        return message_to_client

                if ["greeting:greeting", "check_ticket:check_ticket"]:
                    save_new_conversation = True
                    if save_new_conversation:
                        message_to_client = random.choice(bot_greeting_check_ticket)
                        return message_to_client

                if ["intent_log_ticket:intent_log_ticket", "log_ticket:log_ticket"]:
                    save_new_conversation = True
                    if save_new_conversation:
                        message_to_client = random.choice(bot_intent_log_ticket)
                        return message_to_client
                if [
                    "intent_check_ticket:intention_check_ticket",
                    "check_ticket:check_ticket",
                ]:
                    save_new_conversation = True
                    if save_new_conversation:
                        message_to_client = random.choice(bot_intent_check_ticket)
                        return message_to_client
                if ["intent_log_ticket:intent_log_ticket"]:
                    save_new_conversation = True
                    if save_new_conversation:
                        message_to_client = random.choice(bot_intent_log_ticket)
                        return message_to_client
                if ["intent_check_ticket:intent_check_ticket"]:
                    save_new_conversation = True
                    if save_new_conversation:
                        message_to_client = random.choice(bot_intent_check_ticket)
                        return message_to_client
                if ["log_ticket:log_ticket"]:
                    save_new_conversation = True
                    if save_new_conversation:
                        message_to_client = random.choice(bot_log_ticket)
                        return message_to_client
                if ["check_ticket:check_ticket"]:
                    # that means the user has provided the ticket number and the conversation is now complete
                    # the Ticket number must be sent back to Helpdesk
                    save_new_conversation = True
                    if save_new_conversation:
                        message_to_client = random.choice(bot_check_ticket)
                        return message_to_client

            else:  # it is not a new conversation
                print()

    except:
        pass
    return "200 OK HTTPS."
