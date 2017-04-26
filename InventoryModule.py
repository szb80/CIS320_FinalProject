# CIS320 Final Project
# Gustavo, Hugo & Seth
# SB 4/23

import Validate, Inventory, InventorySQL

ERROR_PROMPT = "**ERROR: That is not a valid selection, try again."

# displays the home page of the Inventory module menu
def displayInventoryMenuHome():
    validMenuChoice = False

    # loop through invalid input for menu display
    while not validMenuChoice:
        # print the menu
        print("INVENTORY MENU", "-" * 20)
        print("1) Check Inventory")
        print("2) Modify Inventory")

        # take user menu choice
        try:
            menuChoice = int(input())
        except ValueError:
            print(ERROR_PROMPT)

        # call sub modules
        if menuChoice == 1:  # check inventory
            validMenuChoice = True
            displayCheckInventoryMenu()
        elif menuChoice == 2:  # modify inventory
            validMenuChoice = True
            displayModifyInventoryMenu()
        else:  # default case
            print(ERROR_PROMPT)


# displays the Check Inventory menu page
def displayCheckInventoryMenu():
    validMenuChoice = False

    while not validMenuChoice:
        # print the menu and take initial input
        itemNumSearch = input("Enter the item number to view (A for all): ")

        # check if itemNumSearch is char for VIEW ALL
        try:
            if str.upper(itemNumSearch) == 'A':
                menuSelection = 0
                validMenuChoice = True  # exit loop and display menu
        except ValueError:
            # catch any error but continue
            print()

        # check if if itemNumSearch is an int, else throw error
        try:
            menuSelection = int(itemNumSearch)  # attempt cast to int
        except ValueError as err:
            print(ERROR_PROMPT, "displayCheckInventoryMenu()", err)

        # menu choice is an int and not ALL, user must want to check item number
        # now check if int is within appropriate range
        inventorySizeParams = Inventory.Inventory()  # create instance to call
        if int(inventorySizeParams.MIN_ITEM_NUMBER_SIZE) \
                <= menuSelection \
                <= int(inventorySizeParams.MAX_ITEM_NUMBER_SIZE):
            validMenuChoice = True  # passes all tests and exits loop

    # input passes all tests; run search and print result
    if menuSelection == 0:
        displayAllInventory()
    else:
        print(searchInventory(menuSelection))


def displayModifyInventoryMenu():
    # displays the Modify Inventory menu
    validMenuChoice = False
    while not validMenuChoice:
        # print the options
        print("(1)  Add Inventory Item")
        print("(2)  Modify Inventory Item")
        print("(3)  Delete Inventory Item")

    return True


def searchInventory(itemNum):
    # searches database for record matching itemNum
    # returns Inventory instance matching itemNum or blank

    if InventorySQL.searchForSQLRecord(itemNum):
        return InventorySQL.createInventoryFromSQLRecord(itemNum)

    return None


def displayAllInventory():
    # displays all inventory in the database


    return True

