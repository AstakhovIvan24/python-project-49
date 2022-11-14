#!/usr/bin/env python3

from random import randint
from random import choice
GAME_POST = "What number is missing in the progression?"
MIN_RANGE = 0
MAX_RANGE = 100
LIST_LEN = 10


def game():
    numbers = list_generation()
    result = str(choice(numbers))
    ind = numbers.index(int(result))
    numbers[ind] = '..'
    question = (' '.join(map(str, numbers)))
    return question, result


def list_generation():
    x = randint(MIN_RANGE, MAX_RANGE)
    y = randint(MIN_RANGE, MAX_RANGE)
    i = 0
    numbers = [x]
    while i < LIST_LEN:
        numbers.append(numbers[i] + y)
        i += 1
    return numbers
