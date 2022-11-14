#!/usr/bin/env python3

from random import randint
GAME_POST = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_RANGE = 0
MAX_RANGE = 100


def game():
    x = randint(MIN_RANGE, MAX_RANGE)
    question = str(x)
    result = is_prime(x)
    return question, result


def is_prime(x):
    if x <= 1:
        return 'no'
    for i in range(2, number):
        if number % i == 0:
            return 'no'
    return 'yes'
