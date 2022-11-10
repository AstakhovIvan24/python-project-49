#!/usr/bin/env python3

import prompt
from brain_games.scripts.core import run_game
from brain_games.games import gcd_game
from random import randint

post = "Find the greatest common divisor of given numbers."


def main():
    run_game(gcd_game)


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


if __name__ == '__main__':
    main()
