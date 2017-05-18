# CIS320 Final Project
# Gustavo, Hugo & Seth
# SB 4/20
import EmployeeSQL, mainMenu
#Global Constants
ERROR_PROMPT = "**ERROR: Employee Not found."
SPACER_SIZE = 20

#import mainMenu

def getEmployeeNumber():  # --------------------------------------------------
    # prompts for employee number to login to program

    returnCondition = False  # set return sentinel

    while not returnCondition:
        try:  # filter non-int input
            userLogin = int(input("Please enter your Employee Number: "))
        except ValueError:
            print("**ERROR: Employee not found!")
            continue

        # check that within range of acceptable employee numbers
        if EmployeeSQL.searchForSQLRecord(userLogin):# #############################################
            print("Thank you!")
            returnCondition = True
            return userLogin

        else:
            print("**ERROR: Out of range!")
            continue  # reset loop



def setManagerFlag(): #---------------------------------------------------
# checks for manager flag in matching employee record
    managerFlag = False  # initialize to default

    empNum = getEmployeeNumber()

    if EmployeeSQL.searchForSQLRecord(empNum):#############################################
        managerFlag = True
        return mainMenu
    elif EmployeeSQL.getEmployeeManagerFlag(empNum)# getEmployeeManagerFlag  #############################################
        managerFlag = False
        return mainMenu(mainMenu.setManagerFlag())
