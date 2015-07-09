# -*- coding: utf-8 -*-
import sys
import re

__author__ = 'yuri shporhun'

with open(sys.argv[1]) as file:
    lines = file.readlines()
    lines = list(filter(lambda x: x != '\n', lines))
    for line in lines:
        processed_line = line.rstrip()
        id_count = 0
        for reg_res in re.findall(r'"id": \d{1,3}, "label"', processed_line):
            number = int(re.search("\d{1,3}", reg_res).group(0))
            id_count += number
        print(id_count)

