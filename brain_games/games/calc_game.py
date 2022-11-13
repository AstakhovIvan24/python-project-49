#!/usr/bin/env python3

from random import randint
from random import choice
GAME_POST = 'What is the result of the expression?'


def game():
    x = randint(0, 10)
    y = randint(0, 10)
    op = ['-', '+', '*']
    make_choice = choice(op)
    operation = {'-': (x - y), '+': (x + y), '*': (x * y)}
    question = (str(x) + ' ' + make_choice + ' ' + str(y))
    result = str(operation[make_choice])
    return question, result
