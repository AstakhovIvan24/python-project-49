#!/usr/bin/env python3

import prompt
from random import randint


def main():
    name = prompt.string('May I have your name? ')
    print ('Hello, ' + name + '!\nAnswer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while 0 <= count <= 2:
        x = randint(1,100)
        question = print ('Question: '+ str(x))
        answer = prompt.string('Your answer: ')
        if x % 2 == 0:
            if answer == 'yes':
                count += 1
                print ('Correct!')
            else:
                print ('\'' + answer + '\' is wrong answer ;(. Correct answer was \'yes\'.\nLet\'s try again,' + name +'!')
                break
        elif x % 2 != 0:
            if answer == 'no':
                count += 1
                print ('Correct!')
            else:
                print ('\'' + answer + '\' is wrong answer ;(. Correct answer was \'no\'.\nLet\'s try again,' + name +'!')
                break
    if count == 3:
        print ('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
