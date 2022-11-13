#!/usr/bin/env python3

from random import randint
GAME_POST = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game():
    x = randint(0, 100)
    result = prime(x)
    question = str(x)
    return question, result


def prime(x):
    k = 0
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            k = k + 1
    if k <= 0:
        return 'yes'
    else:
        return 'no'
