#!/usr/bin/env python3

import prompt
from brain_games.scripts.core import run_game
from brain_games.games import calc_game
from random import randint
from random import choice
post = 'What is the result of the expression?'


def main():
    run_game(calc_game)


def game_rules():
    x = randint(0, 10)
    y = randint(0, 10)
    op = ['-', '+', '*']
    make_choice = choice(op)
    operation = {'-': (x - y), '+': (x + y), '*': (x * y)}
    print('Question: ' + str(x) + ' ' + make_choice + ' ' + str(y))
    answer = prompt.string('Your answer: ')
    result = str(operation[make_choice])
    return answer, result


if __name__ == '__main__':
    main()
