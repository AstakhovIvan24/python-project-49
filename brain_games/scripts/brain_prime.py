#!/usr/bin/env python3

import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n'
          f'Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while 0 <= count < 3:
        x = randint(0, 100)
        y = prime(x)
        print('Question:', x)
        answer = prompt.string('Your answer: ')
        if answer == y:
            count += 1
            print('Correct!')
        else:
            return wrong(answer, y, name)
    if count == 3:
        print('Congratulations, ' + name + '!')


def prime(x):
    k = 0
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            k = k + 1
    if k <= 0:
        return 'yes'
    else:
        return 'no'


def wrong(answer, result, name):
    print(f"'{answer}' is wrong answer ;(."
          f"Correct answer was '{result}'.\n"
          f"Let\'s try again, {name}!")


if __name__ == '__main__':
    main()
