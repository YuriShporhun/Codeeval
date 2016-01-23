#!/usr/bin/python

import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        words = test.rstrip().split(' ');
        max_length = 0
        max_word = ''
        for word in words:
            if len(word) > max_length:
                max_word = word
                max_length = len(word)
        print max_word

main() 