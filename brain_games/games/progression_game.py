#!/usr/bin/env python3

from random import randint
from random import choice
GAME_POST = "What number is missing in the progression?"


def game():
    numbers = list_generation()
    result = str(choice(numbers))
    ind = numbers.index(int(result))
    numbers[ind] = '..'
    question = (' '.join(map(str, numbers)))
    return question, result


def list_generation():
    x = randint(0, 100)
    y = randint(0, 100)
    i = 0
    numbers = [x]
    while i < 10:
        numbers.append(numbers[i] + y)
        i += 1
    return numbers
