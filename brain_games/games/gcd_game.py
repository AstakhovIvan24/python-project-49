#!/usr/bin/env python3

from random import randint

GAME_POST = "Find the greatest common divisor of given numbers."


def game():
    x = randint(1, 100)
    y = randint(1, 100)
    result = str(gcd_recursive(x, y))
    question = (str(x) + ' ' + str(y))
    return question, result


def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)
