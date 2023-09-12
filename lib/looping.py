#!/usr/bin/env python3
import ipdb


def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print('Happy New Year!')

def square_integers(int_list):
    square_int_list = []

    for num in int_list:
        square_int_list.append(num * num)

    return(square_int_list)
    # square_int_list = [(num * num) for num in int_list]
    # print(square_int_list)


def fizzbuzz():
    for num in range(1, 101):
        #if num % 15 == 0:
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)


fizzbuzz()