# CIS320 Final Project
# Gustavo, Hugo & Seth
# SB 4/20

# Imports
import InventoryModule, EmployeesModule, POSModule
import Validate

# Global static for total modules available in program
# Adjust the MAX_MODULES variable when adding additional modules to program.
MAX_MODULES = 3


def getEmployeeNumber():  # --------------------------------------------------
    # prompts for employee number to login to program

    returnCondition = False  # set return sentinel

    while not returnCondition:
        try:  # filter non-int input
            userLogin = int(input("Please enter your Employee Number: "))
        except ValueError:
            print("**ERROR: enter a number!")
            continue

        # check that within range of acceptable employee numbers
        if 1 <= userLogin < 100:  # is within range
            # searchSQLForEmpNumber  #############################################
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

    # searchSQLForEmpNumber  #############################################

    # getEmployeeManagerFlag  #############################################

    return managerFlag


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
            Validate.cls()
            InventoryModule.displayInventoryMenuHome(managerFlag)

        elif menuChoice == 2:
            if managerFlag:
                EmployeesModule.displayPersonnelMenuHome(managerFlag)
            else:
                print("You do not have the appropriate permissions.")

        elif menuChoice == 3:
            POSModule.displayPOSMenuHome(managerFlag)

        elif menuChoice == 0:
            exitProgram = True
            return True  # exit program

        else:
            print("**ERROR: Invalid selection!")

