#!/usr/bin/env python3

from brain_games.cli import welcome_user
import prompt


def run_game(module):
    name = welcome_user()
    print(module.GAME_POST)
    count = 0
    while 0 <= count < 3:
        question, result = module.game()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if answer == result:
            count += 1
            print('Correct!')
        else:
            return print(f"'{answer}' is wrong answer ;(."
                         f"Correct answer was '{result}'.\n"
                         f"Let\'s try again, {name}!")
    if count == 3:
        print('Congratulations, ' + name + '!')
