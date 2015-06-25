#!/usr/bin/python

import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        numbers = test.rstrip()
        numbers = numbers.split(' ')
        first_number = int(numbers[0])
        second_number = int(numbers[1])
        number_length = int(numbers[2])
        for number in range(1, number_length + 1):
            mod_first = False
            mod_second = False

            if number % first_number == 0:
                sys.stdout.write('F')
                mod_first = True

            if number % second_number == 0:
                sys.stdout.write('B') 
                mod_second = True 
            
            if mod_first or mod_second:
                sys.stdout.write(' ')
                continue

            sys.stdout.write(str(number) + ' ')

        print ''

main()