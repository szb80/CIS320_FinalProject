# CIS320 Final Project POS
# Gustavo, Hugo & Seth
#SB 4/30

import Validate, MakingSale, SQLSale

ERROR_PROMPT = "**ERROR: That is not a valid selection, try again."


# displays Home Page of the Point Of Sale (POS) module
def displayPOSMenuHome():
    validPOSMenuChoice = False

    while not validPOSMenuChoice:
        #print POS menu
        print("POS MENU", "-" * 20)
        print("1) Make Sale")
        print("2) Modify Sale")
        print("0) Return")
        
        # take user menu choice
        try:
            menuChoice = int(input())
        except ValueError:
            print(ERROR_PROMPT)
        continue

        # Call sub modules
        if menuChoice == 1: # choose menu item to purchase
            validPOSMenuChoice = True
            displayMakeSaleMenu()
        elif menuChoice == 2: # modify sale
            validPOSMenuChoice = True
            displayModifySaleMenu()
        elif menuChoice == 0
            return True # exit function and return to calling menu
        else: # default case
            print(ERROR_PROMPT)


# displays the POS menu page
def displayPosMenu():
    validMenuChoice = False
    menuSelection = 1

    while not validMenuChoice:
        # print the POS menu and take initial input
        itemNumSearch = input( "Enter the sale item number to view (A for all): " )

        # check if itemNumSearch is for char for VIEW ALL
        try:
            if str.upper(itemNumSearch) == 'A':
                menuSelection = 0
                validMenuChoice = True # exit loop and display menu
        except ValueError:
            # catch any error but continue
            print()

        # check if itemNumSearch in an int, else throw error
        try:
            menuSelection = int(itemNumSearch) # attempt cast to int
        except ValueError as err:
            print(ERROR_PROMPT, "displayPOSMenu()", err)
            continue
            
        inventorySizeParams = Inventory.Inventory()
        if int(inventorySizeParams.MIN_ITEM_NUMBER_SIZE) \
                <= intemNumSearch \
                <= int(inventorySizeParams.MAX_ITEM_NUMBER_SIZE):
            validMenuChoice = True # passes all tests and exits loop
            
    if menuSelection == 0:
        displayAllInventory()
    else:
        
        #### Think I need to change the last few lines to include the Modify Sale functions right???

