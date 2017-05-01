# CIS320 Final Project
# Gustavo, Hugo & Seth
# SB 4/20

# Imports
import InventoryModule

# Initialize variables

# Global static for total modules available in program
# Adjust the MAX_MODULES variable when adding additional modules to program.
MAX_MODULES = 3


# prompts for employee number to login to program
def getEmployeeNumber():
    while True:
        try:
            userLogin = int(input("Please enter your Employee Number: "))
        except ValueError:
            print("Sorry Invalid Input.")
            return getEmployeeNumber()

        if userLogin < 1:
            print("Sorry Invalid Input.")
            return getEmployeeNumber()

        elif userLogin > 100:
            print("Sorry Invalid Input.")
            return getEmployeeNumber()
        else:
            break
    return userLogin


def setManagerFlag(empNum): #---------------------------------------------------
    # checks for manager flag in matching employee record


    return False

# validates if the menu choice was within the appropriate range
def validateMenuChoice(num):
    return num in range(1, MAX_MODULES + 1)


# displays the main menu
# accepts the managerFlag boolean to determine menu display
def mainMenu(managerFlag):
    menuChoice = -1

    # main menu loop, display menu until valid selection is made
    while not validateMenuChoice(menuChoice):
        # print the menu
        print("MAIN MENU", "-" * 20)
        print("1) Inventory")
        if managerFlag:  # only for the bosses!
            print("2) Personnel")
            print("3) POS")
        else:  # sorry, just an employee
            print("3) POS")

        # take the user menu choice
        # validate the input as an int and catch exceptions
        try:
            menuChoice = int(input())
        except ValueError:
            print("Incorrect selection, try again!")


    # call module menus
    if menuChoice == 1:
        InventoryModule.displayInventoryMenuHome()
    elif menuChoice == 2:
        if managerFlag:
            # displayPersonnelMenu()
            print()
        else:
            print("You do not have the appropriate permissions.")
    elif menuChoice == 3:
        print()
        # displayPOSMenu()
    else:
        menuChoice == 0  # invalid menu choice, default to 0

