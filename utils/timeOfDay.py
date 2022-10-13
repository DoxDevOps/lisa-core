import datetime

currentTime = datetime.datetime.now()


def give_me_time_of_day():
    """
    A function that returns time of the day
    :return: -> str
    """
    if currentTime.hour < 12:
        part_of_day = "Morning"
    elif 12 <= currentTime.hour < 18:
        part_of_day = "Afternoon"
    else:
        part_of_day = "Evening"
    return part_of_day
