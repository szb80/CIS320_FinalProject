# CIS320 Final Project
# Hugo & Seth
# SB 4/23

# Validate class to provide global validation functions to other classes

import os

def validateString(phrase):
    if phrase.isdigit():
        return False
    return all(x.isalpha() or x.isspace() for x in phrase)


def validateInt(num):
    try:
        testValue = int(num)
    except ValueError:
        return False
    return True


def validateFloat(num):
    try:
        testValue = float(num)
    except ValueError:
        return False
    return True


def validateFloatOrEmpty(num):
    try:
        if num == "":
            return True  # is empty
    except ValueError:
        return False
    try:
        testValue = float(num)
    except ValueError:
        return False
    return True


def cls():
    # method to clear the console screen
    import subprocess as sp
    t = sp.call('clear', shell=True)
    return
