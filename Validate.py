# CIS320 Final Project
# Hugo & Seth
# SB 4/23

# Validate class to provide global validation functions to other classes


def validateString(phrase):
    return all(x.isalpha() or x.isspace() for x in phrase)


def validateInt(num):
    try:
        testValue = int(num)
    except ValueError:
        return False
    else:
        return True


def validateFloat(num):
    try:
        testValue = float(num)
    except ValueError:
        return False
    else:
        return True
