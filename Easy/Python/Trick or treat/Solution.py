# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sys

WITCH_COEFFICIENT = 5
ZOMBIE_COEFFICIENT = 4
VAMPIRE_COEFFICIENT = 3

test_cases = open(sys.argv[1], 'r')
for line in test_cases:
    tokens = line.rstrip().split(',')
    vampires_count = int(tokens[0].split(':')[1])
    zombies_count = int(tokens[1].split(':')[1])
    witches_count = int(tokens[2].split(':')[1])
    house_count = int(tokens[3].split(':')[1])
    number_of_kids = vampires_count + zombies_count + witches_count
    number_of_candies = (vampires_count * VAMPIRE_COEFFICIENT + zombies_count * ZOMBIE_COEFFICIENT + witches_count * WITCH_COEFFICIENT) * house_count
    number_of_candies_for_each_child = int(number_of_candies / number_of_kids)
    print(number_of_candies_for_each_child)
