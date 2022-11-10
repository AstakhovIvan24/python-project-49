#!/usr/bin/env python3

import prompt
from random import randint
post = "Find the greatest common divisor of given numbers."


def game_rules():
    x = randint(0, 100)
    y = randint(0, 100)
    result = str(gcd_recursive(x, y))
    print('Question: ' + str(x) + ' ' + str(y))
    answer = prompt.string('Your answer: ')
    return answer, result


def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)
