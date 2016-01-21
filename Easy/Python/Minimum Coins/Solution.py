#!/usr/bin/python

import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        number = int(test.rstrip())
        five_coins = int(number / 5)
        number = number % 5
        three_coins = int(number / 3)
        number = number % 3
        number += five_coins + three_coins
        print number
main()