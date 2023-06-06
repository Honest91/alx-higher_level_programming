#!/usr/bin/python3
"""Print all  alphabet in lowercase, but not followed by  new line."""

for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
