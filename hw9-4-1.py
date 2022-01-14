# Author: CMOB 1/14/2022

from email.encoders import encode_noop
import enum


def smash(lst):
    word = None
    for index, value in enumerate(lst):
        word = str(word) + " " + str(value)
    return word



print(smash(['hello','pie','pog','nooooooooo', 'weeeeee',]))