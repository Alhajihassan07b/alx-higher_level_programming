#!/usr/bin/python3
result = ""
for letter in reversed(range(ord('a'), ord('z') + 1)):
    character = chr(letter)
    if letter % 2 != 0:
        result += character.upper()
    else:
        result += character.lower()
print(result)
