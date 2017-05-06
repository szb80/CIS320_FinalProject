# CIS320 Final Project
# Hugo & Seth
# SB 4/23

# Employee class

import Validate


class Employee:

    # set global sizes
    MIN_NUMBER = 1
    MAX_NUMBER = 100


    # initialization def
    def __init__(self
                 , in_empNumber = None
                 , in_empNameFirst = None
                 , in_empNameLast = None
                 , in_empPhone = None
                 , in_manager = False
                 ):

        if in_empNumber is None:
            self.__empNumber = 0  # default case
        else:
            self.__empNumber = in_empNumber  # loaded constructor

        if in_empNameFirst is None:
            self.__empNameFirst = "_BLANK-NAME"  # default case
        else:
            self.__empNameFirst = in_empNameFirst  # loaded constructor

        if in_empNameLast is None:
            self.__empNameLast = "_BLANK-SHORT-DESCRIPTION"  # default case
        else:
            self.__empNameLast = in_empNameLast  # loaded constructor

        if in_empPhone is None:
            self.__empPhone = 0000000000  # default case
        else:
            self.__empPhone = in_empPhone  # loaded constructor

        if in_manager is None:
            self.__manager = False  # default case
        else:
            self.__manager = in_manager  # loaded constructor


    # setters
    def setEmpName(self, first, last):
        # validate both names, set only if both true
        if Validate.validateString(first):
            if Validate.validateString(last):
                self.__empNameFirst = first
                self.__empNameLast = last
                return True
        return False # one or more failed string validation


    def setEmpPhone(self, phone):
        # is phone is valid int, set variable and return true
        if Validate.validateInt(phone):
            self.__empDOB = phone
            return True
        return False


    def setEmpManager(self, isManager):
        # set boolean and return true
        self.__manager = isManager
        return True


    # getters
    def getEmpNumber(self):
        return self.__empNumber


    def getEmpNameFirst(self):
        return str(self.__empNameFirst)


    def getEmpNameLast(self):
        return str(self.__empNameLast)


    def getEmpPhone(self):
        return self.__empPhone


    def getManager(self):
        return self.__manager


    # default print override
    def __str__(self):
        return str("Employee Number: \t"
                   + str(self.__empNumber) + "\n"
                   + "Employee Name: \t\t"
                   + str(self.__empNameFirst)
                   + " "
                   + str(self.__empNameLast) + "\n"
                   + "Employee Phone:\t\t"
                   + str(self.__empPhone) + "\n"
                   + "Is A Manager? \t\t"
                   + str(self.__manager)
                   )
