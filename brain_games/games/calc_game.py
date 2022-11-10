#!/usr/bin/env python3

import prompt
from random import randint
from random import choice
post = 'What is the result of the expression?'


def game_rules():
    x = randint(0, 10)
    y = randint(0, 10)
    op = ['-', '+', '*']
    make_choice = choice(op)
    operation = {'-': (x - y), '+': (x + y), '*': (x * y)}
    print('Question: ' + str(x) + ' ' + make_choice + ' ' + str(y))
    answer = prompt.string('Your answer: ')
    result = str(operation[make_choice])
    return answer, result



# def check_answer(answer, make_choice, x, y):
#     operation = {'-': (x - y), '+': (x + y), '*': (x * y)}
#     return str(operation[make_choice]):
