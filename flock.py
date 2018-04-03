#!/usr/bin/env python
'''
A fuzzy clock
'''
from datetime import datetime

N = datetime.now()
H = N.hour
M = N.minute

NUMBERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
           'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
           'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
           'nineteen', 'twenty']


def to_hours(hrs):
    '''
    Converts hours (integer) to hours (plain English).
    '''
    if hrs % 12 == 0:
        # Pick between noon and midnight
        return ['noon', 'midnight'][hrs // 12 - 1]
    else:
        # Any other hour
        return NUMBERS[hrs % 12 - 1]


def to_minutes(mins):
    '''
    Converts minutes (integer) to minutes (plain English).
    '''
    if mins % 15 == 0:
        # Special minutes - quarters
        return ['quarter', 'half', 'quarter'][mins // 15 - 1]
    elif mins <= len(NUMBERS):
        # Special numbers - single digit (<10)
        return NUMBERS[mins - 1]
    else:
        # Everything else
        return "{}{}".format(
            NUMBERS[mins // 10 - 2],
            ' ' + NUMBERS[mins % 10 - 1] if mins % 10 != 0 else '')


if M == 0:
    # Exactly n o'clock
    print("{}{}".format(to_hours(H),
                        " o'clock" if H % 12 != 0 else ''))
else:
    # All else (hours and minutes)
    MNS = M if M <= 30 else 60 - M
    print("{} {} {}".format(to_minutes(MNS),
                            "past" if M <= 30 else "to",
                            to_hours(H if M <= 30 else H + 1)))
