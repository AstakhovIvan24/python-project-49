#!/usr/bin/env python3

import prompt
from random import randint
from random import choice
post = "What number is missing in the progression?"


def game_rules():
    numbers = list_generation()
    result = str(choice(numbers))
    ind = numbers.index(int(result))
    numbers[ind] = '..'
    print('Question:', *numbers)
    answer = prompt.string('Your answer: ')
    return answer, result


def list_generation():
    x = randint(0, 100)
    y = randint(0, 100)
    i = 0
    numbers = [x]
    while i < 10:
        numbers.append(numbers[i] + y)
        i += 1
    return numbers
