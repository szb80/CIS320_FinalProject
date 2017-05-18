# CIS320 Final Project
# Gustavo, Hugo & Seth
# SB 4/20

# Imports
import InventoryModule, EmployeesModule, POSModule
import EmployeeSQL
import Validate

# Global static for total modules available in program
# Adjust the MAX_MODULES variable when adding additional modules to program.
MAX_MODULES = 3


def getEmployeeNumber():  # tested
    # prompts for employee number to login to program
    # HM

    returnCondition = False  # set return sentinel

    while not returnCondition:
        try:  # filter non-int input
            userLogin = int(input("Please enter your Employee Number: "))
        except ValueError:
            print("**ERROR: Enter an int!")
            continue

        # check that within range of acceptable employee numbers
        if EmployeeSQL.searchForSQLRecord(userLogin):
            returnCondition = True
            return userLogin

        else:
            print("**ERROR: Employee does not exist!")
            continue  # reset loop


def getManagerFlag(empNum): # tested
# checks for manager flag in matching employee record
# HM
    if EmployeeSQL.searchForSQLRecord(empNum):  # if employee exists
        return EmployeeSQL.getEmployeeManagerFlag(empNum)

    return False  # default case


def mainMenu(managerFlag):
# displays the main menu
    exitProgram = False  # loop sentinel
    menuChoice = -1

    # main menu loop, display menu until valid selection is made
    while not exitProgram:
        # print the menu
        print("MAIN MENU", "-" * 20)
        print("(1)  Inventory")
        if managerFlag:  # only for the bosses!
            print("(2)  Personnel")
            print("(3)  POS")
        else:  # just an employee
            print("(3)  POS")
        print("(0)  Quit")

        # take the user menu choice
        # validate the input as an int and catch exceptions
        try:
            menuChoice = int(input())
        except ValueError:
            print("Incorrect selection, try again!")
            continue  # back to the top of loop

        # call module menus
        if menuChoice == 1:
            #Validate.cls()
            InventoryModule.displayInventoryMenuHome(managerFlag)

        elif menuChoice == 2:
            if managerFlag:
                #Validate.cls()
                EmployeesModule.displayPersonnelMenuHome(managerFlag)
            else:
                print("You do not have the appropriate permissions.")

        elif menuChoice == 3:
            #Validate.cls()
            POSModule.displayPOSMenuHome(managerFlag)

        elif menuChoice == 0:
            exitProgram = True
            return True  # exit program

        else:
            print("**ERROR: Invalid selection!")

