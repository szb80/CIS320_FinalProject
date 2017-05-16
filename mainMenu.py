# CIS320 Final Project
# Gustavo, Hugo & Seth
# SB 4/20

# Imports
import InventoryModule, EmployeesModule, POSModule

# Initialize variables
managerFlag = False  # default to false

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
            print("Thank you!")
            returnCondition = True
            return userLogin

        else:
            print("**ERROR: Out of range!")
            continue  # reset loop



def setManagerFlag(): #---------------------------------------------------
# checks for manager flag in matching employee record
    managerFlag = False  # initialize to default

    getEmployeeNumber()

    # searchSQLForEmpNumber

    # getEmployeeManagerFlag

    return managerFlag


def validateMenuChoice(num):
# validates if the menu choice was within the appropriate range
    return num in range(1, MAX_MODULES + 1)


def mainMenu():
# displays the main menu

    menuChoice = -1

    # main menu loop, display menu until valid selection is made
    while not validateMenuChoice(menuChoice):
        # print the menu
        print("MAIN MENU", "-" * 20)
        print("1) Inventory")
        if managerFlag:  # only for the bosses!
            print("2) Personnel")
            print("3) POS")
        else:  # just an employee
            print("3) POS")

        # take the user menu choice
        # validate the input as an int and catch exceptions
        try:
            menuChoice = int(input())
        except ValueError:
            print("Incorrect selection, try again!")
            continue  # back to the top


    # call module menus
    if menuChoice == 1:
        InventoryModule.displayInventoryMenuHome()
    elif menuChoice == 2:
        if managerFlag:
            EmployeesModule.displayPersonnelMenuHome()

        else:
            print("You do not have the appropriate permissions.")
    elif menuChoice == 3:
        print()
        POSModule.displayPOSMenu()  ###########################################
    else:
        mainMenu()  # invalid menu choice, back to top

