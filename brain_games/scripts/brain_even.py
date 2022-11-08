#!/usr/bin/env python3

import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n'
          f'Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while 0 <= count <= 2:
        x = randint(1, 100)
        print('Question: ' + str(x))
        answer = prompt.string('Your answer: ')
        if x % 2 == 0:
            if answer == 'yes':
                count += 1
                print('Correct!')
            else:
                result = 'yes'
                return wrong(answer, result, name)
        elif x % 2 != 0:
            if answer == 'no':
                count += 1
                print('Correct!')
            else:
                result = 'no'
                return wrong(answer, result, name)
    if count == 3:
        print('Congratulations, ' + name + '!')


def wrong(answer, result, name):
    return print(f"'{answer}' is wrong answer ;(."
                 f"Correct answer was '{result}'.\n"
                 f"Let\'s try again, {name}!")


if __name__ == '__main__':
    main()
