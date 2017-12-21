#!/usr/bin/env python
from datetime import datetime

n = datetime.now()
h = n.hour
m = n.minute

HOURS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
         'eight', 'nine', 'ten', 'eleven', 'twelve']

TEES = ['twenty', 'thirty', 'fourty', 'fifty']


def to_hours(hrs):
    if hrs % 12 == 0:
        return ['noon', 'midnight'][hrs // 12 - 1]
    else:
        return HOURS[hrs % 12 - 1]


def to_minutes(mns):
    if mns <= len(HOURS):
        return HOURS[mns - 1]
    elif mns % 15 == 0:
        return ['quarter', 'half', 'quarter'][mns // 15 - 1]
    elif mns < 20:
        return (HOURS[mns - 11] + "teen").replace('tt', 't')
    elif mns % 10 == 0:
        return TEES[mns // 10 - 2]
    else:
        return "{} {}".format(
            TEES[mns // 10 - 2],
            HOURS[mns % 10 - 1])


if m == 0:
    if h % 12 == 0:
        print(to_hours(h))
    else:
        print("{} o'clock".format(to_hours(h)))
else:
    mns = m if m <= 30 else 60 - m
    print("{} {} {}".format(
        to_minutes(mns),
        "past" if m <= 30 else "to",
        to_hours(h if m <= 30 else h + 1)))
