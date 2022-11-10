#!/usr/bin/env python3

from brain_games.scripts.cli import welcome_user


def run_game(game):
    name = welcome_user()
    print(game.post)
    count = 0
    while 0 <= count < 3:
        answer, result = game.game_rules()
        if answer == result:
            count += 1
            print('Correct!')
        else:
            return print(f"'{answer}' is wrong answer ;(."
                         f"Correct answer was '{result}'.\n"
                         f"Let\'s try again, {name}!")
    if count == 3:
        print('Congratulations, ' + name + '!')
