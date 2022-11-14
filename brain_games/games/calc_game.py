#!/usr/bin/env python3

from random import randint
from random import choice
GAME_POST = 'What is the result of the expression?'
MIN_RANGE = 0
MAX_RANGE = 10


def game():
    x = randint(MIN_RANGE, MAX_RANGE)
    y = randint(MIN_RANGE, MAX_RANGE)
    operators = ['-', '+', '*']
    make_choice = choice(operators)
    operation = {'-': (x - y), '+': (x + y), '*': (x * y)}
    question = (str(x) + ' ' + make_choice + ' ' + str(y))
    result = str(operation[make_choice])
    return question, result
