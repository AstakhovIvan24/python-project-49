#!/usr/bin/env python3

import prompt
from random import randint
from random import choice


def main():
    print('Welcome to the Brain Games!')
    brain_calc()


def brain_calc():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!\nWhat is the result of the expression?')
    count = 0
    while 0 <= count <= 2:
        x = randint(0, 100)
        y = randint(0, 100)
        op = ['-', '+', '*']
        make_choice = choice(op)
        print('Question: ' + str(x) + ' ' + make_choice + ' ' + str(y))
        answer = prompt.string('Your answer: ')
        if check_answer(answer, make_choice, x, y) is True:
            count += 1
            print('Correct!')
        else:
            return wrong(answer, check_answer(answer, make_choice, x, y), name)
    if count == 3:
        print('Congratulations, ' + name + '!')


def check_answer(answer, make_choice, x, y):
    operation = {'-': (x - y), '+': (x + y), '*': (x * y)}
    if answer == str(operation[make_choice]):
        return True
    else:
        return str(operation[make_choice])


def wrong(answer, result, name):
    return print(f"'{answer}' is wrong answer ;(."
                 f"Correct answer was '{result}'.\n"
                 f"Let\'s try again, {name}!")


if __name__ == '__main__':
    main()
