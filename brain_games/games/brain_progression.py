#!/usr/bin/env python3

import prompt
from random import randint
from random import choice


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!\n"
          f"What number is missing in the progression?")
    count = 0
    while 0 <= count < 3:
        numbers = list_generation()
        make_choice = choice(numbers)
        ind = numbers.index(int(make_choice))
        numbers[ind] = '..'
        print('Question:', *numbers)
        answer = prompt.string('Your answer: ')
        if answer == str(make_choice):
            count += 1
            print('Correct!')
        else:
            result = make_choice
            return wrong(answer, result, name)
    if count == 3:
        print('Congratulations, ' + name + '!')


def list_generation():
    x = randint(0, 100)
    y = randint(0, 100)
    i = 0
    numbers = [x]
    while i < 10:
        numbers.append(numbers[i] + y)
        i += 1
    return numbers


def wrong(answer, result, name):
    return print(f"'{answer}' is wrong answer ;(."
                 f"Correct answer was '{result}'.\n"
                 f"Let\'s try again, {name}!")


if __name__ == '__main__':
    main()
