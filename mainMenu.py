# CIS320 Final Project
# Hugo & Seth
# SB 4/20


MAX_MODULES = 3  # Global static for total modules in program

menuChoice = 0  # initialize


def getMenuModules(selection):
    menuModules = {
        '1': "Inventory",
        '2': "Personnel",
        '3': "POS"
    }[selection]
    return menuModules


# tested okay
def validateMenuChoice(num):
    return num in range(1, MAX_MODULES + 1)


################################################################################
# BEGIN INVENTORY MODULE
################################################################################
def goInventoryMenu():
    imenuChoice = 0

    while not validateMenuChoice(imenuChoice):
        # print the menu
        print("INVENTORY MENU", "-" * 20)
        print("1) Check Inventory")
        print("2) Modify Inventory")

        # take user menu choice
        menuChoice = int(input())  # CATCH EXCEPTION #########################################

        # call sub modules
        if menuChoice == 1:
            print()
        elif menuChoice == 2:
            print()
        else:
            menuChoice == 0  # reset to 0 and start over



################################################################################
# END INVENTORY MODULE
################################################################################


def mainMenu():
    # main menu loop, display menu until valid selection is made
    while not validateMenuChoice(menuChoice):
        # print the menu
        print("MAIN MENU", "-" * 20)
        print("1) Inventory")
        print("2) Personnel")
        print("3) POS")

        # take the user menu choice
        menuChoice = int(input())  # CATCH EXCEPTION ++++++++++++++++++++++++++++++++++++++

        # call module menus
        if menuChoice == 1:
            goInventoryMenu()
        elif menuChoice == 2:
            print()
            # goPersonnelMenu()
        elif menuChoice == 3:
            print()
            # goPOSMenu()
        else:
            menuChoice == 0  # invalid menu choice, default to 0


mainMenu()

