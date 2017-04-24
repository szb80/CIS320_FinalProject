# CIS320 Final Project
# Hugo & Seth
# SB 4/23

import Validate, Inventory, sqlite3

def displayInventoryMenu():
    validMenuChoice = False

    while not validMenuChoice:
        # print the menu
        print("INVENTORY MENU", "-" * 20)
        print("1) Check Inventory")
        print("2) Modify Inventory")

        # take user menu choice
        try:
            menuChoice = int(input())
        except ValueError:
            print("Incorrect selection, try again!")
        else:
            # call sub modules
            if menuChoice == 1:  # check inventory
                validMenuChoice = True
                print() ##############################################
            elif menuChoice == 2:  # modify inventory
                validMenuChoice = True
                print() ##############################################

# displays the Check Inventory menu
def checkInventoryMenu():
    validMenuChoice = False

    while not validMenuChoice:
        # print the menu
        print("Enter the item number to view: ")
        # "Or (S) to Search" ###################################################
        try:
            itemNumSearch = int(input("Enter the item number to view: "))
        except ValueError:
            print("That is not a number, try again.")
        else:
            Inventory.displayInventory(Inventory.searchInventory(itemNumSearch))

