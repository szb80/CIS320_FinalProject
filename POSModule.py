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

        try:
            menuChoice = int(input())
        except ValueError:
            print(ERROR_PROMPT)

        # Call sub modules
        if menuChoice == 1:
            validPOSMenuChoice = True
            displayMakeSaleMenu()
        elif menuChoice == 2: # modify sale
            validPOSMenuChoice = True
            displayModifySaleMenu()
        else: # default case
            print(ERROR_PROMPT)


# displays the POS menu page
def displayPosMenu():
    validMenuChoice = False

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
            


