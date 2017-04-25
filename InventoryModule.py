# CIS320 Final Project
# Hugo & Seth
# SB 4/23

import Validate, Inventory, sqlite3

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
        # print the menu
        print("Enter the item number to view (A for all): ")

        # take initial input
        itemNumSearch = input("Enter the item number to view: ")

        # check if itemNumSearch is char for SEARCH or VIEW ALL
        try:
            if str.upper(itemNumSearch) == 'A':  # exit loop and display menu
                validMenuChoice = True
                displayAllInventory()
        except ValueError:
            print()
        # print(ERROR_PROMPT) #############################################
        # would display even if a valid item number is passed!!!!!

        # check if if itemNumSearch is an int, else throw error
        try:
            menuSelection = int(itemNumSearch)  # attempt cast to int
        except ValueError:
            print(ERROR_PROMPT)

        # menu choice is an int and not ALL, user must want to check item number
        # now check if int is within appropriate range
        # prevents wild or negative number input
        if itemNumSearch >= Inventory.getMIN_ITEM_NUMBER_SIZE:
            validMenuChoice = True
        elif itemNumSearch <= Inventory.getMAX_ITEM_NUMBER_SIZE:
            validMenuChoice = True

    # input passes all tests and is safe to pass to searchInventory()
    searchInventory(itemNumSearch)

def displayModifyInventoryMenu():
    validMenuChoice = False

    while not validMenuChoice:
        # print the options
        print("(1)  Add Inventory Item")
        print("(2)  Modify Inventory Item")
        print("(3)  Delete Inventory Item")

    return True




def searchInventory(itemNum):
    # SEARCHES INVENTORY DB FOR ITEM NUM MATCHING ARGUMENT #################
    # read inventory record to variable
    # convert SQL to inventory object
    # returns matching inventory instance ##################################
    return True


def displayAllInventory():
    # displays all inventory in the database
    return True





###### CURRENTLY UNUSED IN SPEC ############################################
def searchInventory(searchStr):
    # SEARCHES INVENTORY DB FOR NAME MATCHING searchStr  ###################
    # returns matching inventory instance ##################################
    return True