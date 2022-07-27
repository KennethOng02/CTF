#!/usr/bin/env python3

import string

key = "VOUHMJLTESZCDKWIXNQYFAPGBR"

with open("message.txt") as f:
    content = f.read()

for char in content:
    if char.isalpha():
        position = key.index(char.upper())
        if char.isupper():
            print(string.ascii_uppercase[position], end='')
        else:
            print(string.ascii_lowercase[position], end='')
    else:
        print(char, end='')
