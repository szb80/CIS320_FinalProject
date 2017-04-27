# CIS320 Final Project
# Hugo & Seth
# SB 4/23

# Employee class

import Validate


class Employee:

    # set global sizes
    MIN_NUMBER_SIZE = 1
    MAX_NUMBER_SIZE = 100


    # initialization def
    def __init__(self):
        self.__empNumber = 000
        self.__empNameFirst = "_BLANK NAME"
        self.__empNameLast = "_BLANK LAST NAME"
        self.__empPhone = "1234567890"
        self.__manager = False


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

        if in_itemName is None:
            self.__itemName = "_BLANK-NAME"  # default case
        else:
            self.__itemName = in_itemName  # loaded constructor

        if in_itemDesc is None:
            self.__itemDesc = "_BLANK-SHORT-DESCRIPTION"  # default case
        else:
            self.__itemDesc = in_itemDesc  # loaded constructor

        if in_stockCount is None:
            self.__stockCount = 0  # default case
        else:
            self.__stockCount = in_stockCount  # loaded constructor

    def setEmpName(self, first, last):
        # validate both names, set only if both true
        if Validate.validateString(first):
            if Validate.validateString(last):
                self.__empNameFirst = first
                self.__empNameLast = last
                return True
        return False # one or more failed validation as strings


    def setEmpDOB(self, date):
        if Validate.validateInt(date):
            self.__empDOB = date
            return True
        return False


    def setEmpDOB(self, dob):
        if Validate.validateInt(dob):
            self.__empDOB = dob
            return True
        return False


    def __str__(self):
        print("Employee Number:  #", self.__empNumber
              , "\nEmployee Name:  "
              , self.__empNameFirst
              , " "
              , self.__empNameLast
              , "\nEmployee DOB:  "
              , self.__empDOB  ######## process DOB function ###################
              , "\nEmployee Phone:  ("
              , self.__empPhone # process phone function #######################
              , sep = '')


    def displayEmployee(self):
        str(self)


    def displayInventory(self, empNum):  ######################################
        self.searchEmployee(empNum)  # search for item number and
        self.displayEmployee(empNum)  # display for returned inventory item



