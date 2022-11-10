#!/usr/bin/env python3

import prompt
from random import randint
post = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_rules():
    x = randint(0, 100)
    result = prime(x)
    print('Question:', x)
    answer = prompt.string('Your answer: ')
    return answer, result


def prime(x):
    k = 0
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            k = k + 1
    if k <= 0:
        return 'yes'
    else:
        return 'no'
