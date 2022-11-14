#!/usr/bin/env python3

from random import randint

GAME_POST = "Find the greatest common divisor of given numbers."
MIN_RANGE = 1
MAX_RANGE = 100


def game():
    x = randint(MIN_RANGE, MAX_RANGE)
    y = randint(MIN_RANGE, MAX_RANGE)
    result = str(gcd_recursive(x, y))
    question = (str(x) + ' ' + str(y))
    return question, result


def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)
