#!/usr/bin/python3
def multiple_returns(sentence):
    length = ()
    if len(sentence) == 0:
        length = 0, "None"
    else:
        length = len(sentence), sentence[0]
    return length
