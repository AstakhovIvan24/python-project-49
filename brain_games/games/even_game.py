#!/usr/bin/env python3

from random import randint


GAME_POST = 'Answer "yes" if the number is even, otherwise answer "no".'


def game():
    x = randint(1, 100)
    question = str(x)
    if x % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return question, result
