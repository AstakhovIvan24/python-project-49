#!/usr/bin/env python3

import prompt
from random import randint

def main():
    print ('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print ('Hello, ' + name + '!\nFind the greatest common divisor of given numbers.')
    count = 0
    while 0 <= count <3:
        x = randint(0,100)
        y = randint(0,100)
        gcd = gcd_recursive(x,y)
        question = print ('Question: '+ str(x) + ' ' + str(y))
        answer = prompt.string('Your answer: ')
        if int(answer) == gcd_recursive(x,y):
            count += 1
            print ('Correct!')
        else:
            result = str(gcd)
            return wrong(answer,result, name)
            
    if count == 3:
        print ('Congratulations, ' + name + '!')

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

def wrong(answer, result, name):
    return print ('\'' + answer + '\' is wrong answer ;(. Correct answer was \'' + result +'\'.\nLet\'s try again,' + name +'!')

if __name__ == '__main__':
    main()