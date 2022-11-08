#!/usr/bin/env python3

import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    brain_even()


def brain_even():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n'
          f'Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while 0 <= count <= 2:
        x = randint(1, 100)
        print('Question: ' + str(x))
        answer = prompt.string('Your answer: ')
        if answer == check_even(x):
            count += 1
            print('Correct!')
        else:
            return wrong(answer, check_even(x), name)
    if count == 3:
        print('Congratulations, ' + name + '!')


def check_even(x):
    if x % 2 == 0:
        return 'yes'
    else:
        return 'no'


def wrong(answer, result, name):
    return print(f"'{answer}' is wrong answer ;(."
                 f"Correct answer was '{result}'.\n"
                 f"Let\'s try again, {name}!")


if __name__ == '__main__':
    main()
