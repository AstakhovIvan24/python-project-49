#!/usr/bin/env python3

from random import randint


GAME_POST = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_RANGE = 1
MAX_RANGE = 100


def game():
    x = randint(MIN_RANGE, MAX_RANGE)
    question = str(x)
    if x % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return question, result
