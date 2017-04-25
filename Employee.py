# CIS320 Final Project
# Hugo & Seth
# SB 4/23

# Employee class

import Validate


class Employee:

    # set global sizes
    MIN_NUMBER_SIZE = 1
    MAX_NUMBER_SIZE = 99

    # initialization def
    def __init__(self):
        self.__empNumber = 000
        self.__empNameFirst = "_BLANK NAME"
        self.__empNameLast = "_BLANK LAST NAME"
        self.__empDOB = "01010000"
        self.__empPhone = "1234567890"
        self.__manager = False


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


    def searchEmployee(self, searchStr):
        # SEARCHES DB FOR NAME MATCHING searchStr  ############################
        # returns matching employee instance ##################################
        return True



