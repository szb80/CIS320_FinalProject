# CIS320 Final Project
# Hugo & Seth
# SB 4/23

# Sale class

import Validate, datetime

# Initialize variables


class Sale:

    # initialization def
    def __init__(self):
        self.__saleNumber = datetime.datetime.now(datetime.timezone.utc)
        self.__lineItem = []


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
        return True


    def searchEmployee(self, searchStr):
        # SEARCHES DB FOR NAME MATCHING searchStr  ###################
        # returns matching employee instance ##################################
        return True


