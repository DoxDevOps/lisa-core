import datetime
import random


from apps.chatbot.witChat import response_from_wit, process_response_from_wit
from config.config import config
from utils.botResponse import intent_response
from utils.conversationOccurances import possible_conversations

# from utils.databaseOperations import check_last_conversation, check_if_number_exist, save_conversation

# *********Config*******************
token = config["token"]
response_message: str = config["response_message"]
facebook_url = config["facebook_url"]
helpdesk_url = config["helpdesk_url"]

# ********* Intents ************
bot_null_response = intent_response["null"]
bot_greeting_response = intent_response["greeting:greeting"]
bot_greeting_log_intent = intent_response["greeting:greeting,intent_log_ticket:intent_log_ticket"]
bot_greeting_check_intent = intent_response["greeting:greeting,intent_check_ticket:intent_check_ticket"]
bot_greeting_intent_log_ticket = intent_response[
    "greeting:greeting,intent_log_ticket:intent_log_ticket,log_ticket:log_ticket"]
bot_greeting_intent_check_ticket = intent_response["greeting:greeting,intent_check_ticket:intention_check_ticket," \
                                                   "check_ticket:check_ticket"]
bot_greeting_log_ticket = "greeting:greeting,log_ticket:log_ticket"
bot_greeting_check_ticket = "intent_log_ticket:intent_log_ticket,log_ticket:log_ticket"
bot_intent_log_ticket = "intent_log_ticket:intent_log_ticket,log_ticket:log_ticket"
bot_intent_check_ticket = "intent_check_ticket:intent_check_ticket"
bot_log_ticket = "log_ticket:log_ticket"
bot_check_ticket = "check_ticket:check_ticket"

bot_conversations = possible_conversations["possible_conv"]


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
            message_to_sender = random.choice(bot_null_response)  # get a random response
            return message_to_sender
        else:
            # check if the user already started a conversation
            # check_conversation = check_last_conversation(phone_number)
            new_conversation = True  # check_if_number_exist(phone_number)
            # if user_id and not check_conversation:
            if new_conversation:
                # that means it is a new conversation
                if ["greeting:greeting"] == entity:
                    save_new_conversation = True #  send to the database

                    if save_new_conversation:
                        # send the user a response message
                        greetings_message_to_sender = random.choice(bot_greeting_response)  # get a random response
                        return greetings_message_to_sender

                if ["greeting:greeting", "intent_log_ticket:intent_log_ticket"] == entity:
                    save_new_conversation = True #  send to the database
                    if save_new_conversation:
                        message_to_client = random.choice(bot_greeting_log_intent)
                        return message_to_client

                if ["greeting:greeting", "intent_check_ticket:intent_check_ticket"] == entity:
                    save_new_conversation = True
                    if save_new_conversation:
                        message_to_client = random.choice(bot_greeting_check_intent)
                        return message_to_client
                if ["greeting:greeting", "intent_log_ticket:intent_log_ticket", "log_ticket:log_ticket"]:
                    save_new_conversation = True
                    if save_new_conversation:
                        message_to_client = random.choice(bot_greeting_intent_log_ticket)
                        return message_to_client

                if ["greeting:greeting", "intent_check_ticket:intention_check_ticket", "check_ticket"
                                                                                       ":check_ticket"]:
                    save_new_conversation = True
                    if save_new_conversation:
                        message_to_client = random.choice(bot_greeting_intent_check_ticket)
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
                if ["intent_check_ticket:intention_check_ticket", "check_ticket:check_ticket"]:
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
                    save_new_conversation = True
                    if save_new_conversation:
                        message_to_client = random.choice(bot_check_ticket)
                        return message_to_client


            else:  # it is not a new conversation
                print("yewo")

        """if entity == "greeting:greeting":
                print("INSIDE Greeting !!")
                message_to_sender1 = random.choice(bot_greeting_response)
                print(message_to_sender1)
                send_msg_to_client(phone_number, message_to_sender1)

                print(entity == "log_ticket:log_ticket")
                message_to_sender = process_response_from_wit(entity)
                print(message_to_sender)
                # 2. send it to help desk
                response_from_helpdesk = requests.get(helpdesk_url + complete_message)
                # 3. depending on the response from helpdesk, send back the response to the user/sender
                send_msg_to_client(phone_number, message_to_sender)
                send_msg_to_client(phone_number)
                print(" Printing Response from Helpdesk SIRRRR !!")
                print(response_from_helpdesk)"""
        # return 'Ok', 200
    except:
        pass
    return '200 OK HTTPS.'


def process_new_conversation(intent_check_ticket, log_ticket, check_ticket, user_id, greeting, intent_log_ticket):
    """conversation.intent_check_ticket = intent_check_ticket
    conversation.log_ticket = log_ticket
    conversation.check_ticket = check_ticket
    conversation.user_id = user_id
    conversation.date = datetime.date
    conversation.greeting = greeting
    conversation.intent_log_ticket = intent_log_ticket
    try:
        save_new_conversation = save_conversation(conversation)
        if save_new_conversation:
            return True
    except:
        return False"""
    return True
