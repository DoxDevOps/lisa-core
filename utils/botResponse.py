import os

from timeOfDay import give_me_time_of_day
from dotenv import load_dotenv


load_dotenv()  # load .env file


part_of_day = give_me_time_of_day()
bot_name = os.environ.get("bot_name")

intent_response = \
    {
        "null": ["I am sorry, i dont understand you. Msy you please rephrase your statement ?",
                 "Please be clear. I can only help you with logging a ticket or check for a ticket",
                 "Pardon ?",
                 "Come again please ",
                 "Sorry, i seem not to understand you . You can start a conversation with me using :\n"
                 "1. Hi " + bot_name + " or just Hello \n 2. I would like to log a ticket"
                                       " 3. I want to check for a ticket",
                 "Well, i do not what you want. I only log tickets and check for tickets in Helpdesk",
                 "What do you mean ? please be clear, at least choose one : \n1. log a ticket \n2. check for a ticket "
                 "!! "
                 ],
        "greeting:greeting": [
            "Hello, my name is " + bot_name + ", your Helpdesk Assistant. \n Currently i can do the following : \n"
                                              "1. Help you log a ticket/ issue in helpdesk \n 2. Search a ticket you "
                                              "opened ",

            "Good " + part_of_day + " ! I am " + bot_name + " your Technical Assistant\n"
                                                            "I can help you log a ticket and search for a ticket on "
                                                            "Helpdesk. "
                                                            " What can i do for you this " + part_of_day,

            "Hi, welcome to Helpdesk. I am " + bot_name + ". Would you like to log a ticket "
                                                          "or search for a ticket.",

            "What a good " + part_of_day + " !! its " + bot_name + " here, what can i do for you ?",

            "I am " + bot_name + ", your Support Assistant. This " + part_of_day + "i can help you with creating a "
                                                                                   "ticket or "
                                                                                   "searching for a ticket. What "
                                                                                   "would you like me "
                                                                                   "to do for you this " + part_of_day],
        "log_ticket:log_ticket": [
            "Great choice, let me help you Log your query. Wait for a issue number please",
            "I can do that, just give me a minute. I will send you a ticket number shortly",
            "Sure, let me do that for you. Please wait for a ticket or issue number",
            "I am here to help you do that. Let me work on it. give me about 2 minutes.\n"
            "Please wait for a ticket number",
            "Let me do that for you this " + part_of_day + ". Wait for your issue number please !! "],

        "appreciate:appreciate": ["You are welcome !!", " I am glad I could help !",
                                  "Any time ! have a good " + part_of_day,
                                  "Cheers !!", "Bye ! have a good " + part_of_day,
                                  "No problem, i enjoyed helping you !!",

                                  "The pleasure is mine !! bye.",
                                  "My pleasure! Have a good " + part_of_day,
                                  "NO worries !!",
                                  "Dont mention it, have a good " + part_of_day,
                                  "It is the least i could do for you !!",
                                  "I am glad i could help"],

        "intent_log_ticket:intent_log_ticket": ["No problem. Whats seems to be the problem ?",
                                                "am glad to help you log your ticket. Send the send the issue",
                                                "Gladly, what seems to be the problem that side ?",
                                                "I can do that for you !! What is the problem ?",
                                                "Sure, what seems to be the problem ?",
                                                "I am glad to process your concerns ! please be clear, what seems to "
                                                "be the problem ? "
                                                ],

        "intent_check_ticket:intent_check_ticket": [
            "It looks like you want to log a ticket, may you please give me the "
            "ticket number !",
            "Great, please send me the ticket number",
            "What is your ticket number ?",
            "No problem, give me your ticket number then ",
            "I can do that, give me your ticket number",
            "Awesome ! give me your ticket number then !",
            "That's alright, give me your Issue number ",
            "Send your ticket number then !"],

        "check_ticket:check_ticket": ["Thank you for submitting your ticket number. Let me it for you.",
                                      "Let me the ticket for you",
                                      "I will check the details for you. just wait a minute",
                                      "Thank you, give me a minute, let me search !!"],

        "greeting:greeting,intent_log_ticket:intent_log_ticket": [
            "Good " + part_of_day + " Send your query then !",
            " Hello, may you send the problem please !",
            "Hi, what seems to be the problem at your facility ?",
            "Yes !! Tell me your problem",
            "I am here to help you. What seems to be the problem at your facility or site ?",
            " Hello, let me know what the problem is and i will log it for you"],

        "greeting:greeting,intent_check_ticket:intent_check_ticket":
            ["I hope you are well, send me your ticket number",
             "hello, Send me your ticket number",
             "Hi, what is your ticket number",
             "What is your issue number ? "],
        "greeting:greeting,intent_log_ticket:intent_log_ticket,log_ticket:log_ticket":
            [
                "Awesome !! I hope you are well, let me log the ticket for you. please wait for a ticket number !",
                "Hello, Thank you for your request. let me log the issue and please wait for a ticket number",
                "Hi, am glad to help you. please wait for a ticket number ",
                "Greeting, let me log the issue for you and please wait fo a ticket number",
                "I hope you are well, let me log the issue for you. please wait for a ticket number",
                "Hi, log your issue in our system. HIS officers will reach out to you shortly. please wait for a "
                "ticket number",
                "hello, I am logging your issue in our system. Our Team will come and rescue you shortly",
                "Hello hello !! i am glad to hear from yu. Let me log your problem in our system. You will receive "
                "feedback from our TEAM shortly "
            ],
        "greeting:greeting,intent_check_ticket:intention_check_ticket,check_ticket:check_ticket":
            [
                "Hi, thank you for being direct. let me check if your ticket is still open. I will send you the "
                "details shortly ",
                "Great, let me check your ticket in our system . \n Cheers !!",
                "Cheers !! Let me check your ticket. gie me 2 minutes please",
                "Hello, thank you for following up. let me check if the issue was solved or not"
            ],

        "greeting:greeting,log_ticket:log_ticket":
            [
                "Hi, let me log your ticket, please wait",
                "Hello, thank you for reaching out. let me log your ticket. please wait for ticket number",
                "Greetings, i hope you are well ! let me log the issue for you in help desk",
                "I hope you are well, let me log the ticket for you",
                "Hi, am always happy to help you. Let me log the ticket for you",
                "Let me log your issue shortly, please wait for a ticket number "
            ],
        "greeting:greeting,check_ticket:check_ticket":
            [
                "Hi, let me check your ticket, please wait",
                "Hello, thank you for reaching out. let me check your ticket. please wait for details",
                "Greetings, i hope you are well ! let me check the issue for you in help desk",
                "I hope you are well, let me check the ticket for you",
                "Hi, am always happy to help you. Let me check the ticket for you",
                "Let me check your issue shortly, please wait for details."
            ],
        "intent_log_ticket:intent_log_ticket,log_ticket:log_ticket":
            [
                "Let me log your ticket, please wait",
                "Thank you for reaching out. let me log your ticket. please wait for ticket number",
                "Let me log the issue for you in help desk",
                "Let me log the ticket for you",
                "Am always happy to help you. Let me log the ticket for you",
                "Let me log your issue shortly, please wait for a ticket number "
            ],
        "intent_check_ticket:intention_check_ticket,check_ticket:check_ticket":
            [
                "Let me check your ticket. please wait !",
                "NO problem, let mw help you with that",
                "Am glad to do that for you please wait for about 5 minutes."
                "Lets see what i can do. let me check in the system. i will get back to you shortly",
                "Sure, let me check your ticket. please wait",
                "Alright, let me check the ticket for you then"
            ]

    }
