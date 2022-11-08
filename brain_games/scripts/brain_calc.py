#!/usr/bin/env python3

import prompt
from random import randint
from random import choice


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!\nWhat is the result of the expression?')
    count = 0
    while 0 <= count <= 2:
        x = randint(0, 100)
        y = randint(0, 100)
        op = ['-', '+', '*']
        operation = {'-': (x - y), '+': (x + y), '*': (x * y)}
        make_choice = choice(op)
        print('Question: ' + str(x) + make_choice + str(y))
        answer = prompt.string('Your answer: ')
        if make_choice == '-':
            if answer == str(x - y):
                count += 1
                print('Correct!')
            else:
                result = str(x - y)
                return wrong(answer, result, name)
        elif make_choice == '+':
            if answer == str(x + y):
                count += 1
                print('Correct!')
            else:
                result = str(x + y)
                return wrong(answer, result, name)
        elif make_choice == '*':
            if answer == str(x * y):
                count += 1
                print('Correct!')
            else:
                result = str(x * y)
                return wrong(answer, result, name)
        else:
            result = str(operation[make_choice])
            return wrong(answer, result, name)
    if count == 3:
        print('Congratulations, ' + name + '!')


def wrong(answer, result, name):
    return print(f"'{answer}' is wrong answer ;(."
                 f"Correct answer was '{result}'.\n"
                 f"Let\'s try again,{name}!")


if __name__ == '__main__':
    main()
