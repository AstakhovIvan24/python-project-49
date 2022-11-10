#!/usr/bin/env python3

import prompt
from random import randint

post = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_rules():
    x = randint(1, 100)
    print('Question: ' + str(x))
    answer = prompt.string('Your answer: ')
    result = check_even(x)
    return answer, result


def check_even(x):
    if x % 2 == 0:
        return 'yes'
    else:
        return 'no'
