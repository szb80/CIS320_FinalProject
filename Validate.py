# CIS320 Final Project
# Hugo & Seth
# SB 4/23

# Validate class to provide global validation functions to other classes

import os  # for clear screen method

def validateString(phrase):
    # checks if argument is a string (letters only)
    if phrase.isdigit():
        return False
    return all(x.isalpha() or x.isspace() for x in phrase)


def validateInt(num):
    # checks if argument is an int
    try:
        testValue = int(num)
    except ValueError:
        return False
    return True


def validateFloat(num):
    # checks is argument is a float
    try:
        testValue = float(num)
    except ValueError:
        return False
    return True


def validateFloatOrEmpty(num):
    # checks if argument is a float or emptuy
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
    # works on Windows OS only.  Program is only supported on Windows.
    clear = lambda: os.system('cls')
    clear()
    return
