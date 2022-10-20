# Modules
import random


# from typing import Dict, List


# expected intents
# for new intents, simple add them to this dict and everything will still hold


def respond_to_intent(
        intents_from_nlp_engine: list,
        expected_intents: dict,
        intent_response: dict,
) -> str:
    """responds to a user's intent

    Args:
        intents_from_nlp_engine (list[str]): intents from the NLP engine
        expected_intents (dict[int, dict]): intents that we are expecting to come in
        intent_response (dict[str, list]): possible responses

    Returns:
        str: response chosen randomly
    """
    print(intents_from_nlp_engine)
    print(type(intents_from_nlp_engine))

    intents_from_nlp_engine = list(intents_from_nlp_engine)
    responses = []

    if not intents_from_nlp_engine:
        return random.choice(intent_response["null"])

    for intent_from_nlp_engine in intents_from_nlp_engine:
        for expected_intent in expected_intents:
            if intent_from_nlp_engine == expected_intents[expected_intent]["intent"][0]:
                responses.append(intent_from_nlp_engine)

    # turn responses to strings separated by commas
    # check if responses is not empty
    # if empty, return default response
    resp = ",".join(responses) if responses else "null"
    if resp != "null":
        for each_intent_response in intent_response:
            if sorted(each_intent_response) == sorted(resp):
                return random.choice(intent_response[each_intent_response])

    return random.choice(intent_response[resp])
