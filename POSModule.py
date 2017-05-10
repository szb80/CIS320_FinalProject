# CIS320 Final Project POS
# Gustavo, Hugo & Seth
#SB 4/30

import Validate, Sale, SaleSQL, mainMenu

# global constants
ERROR_PROMPT = "**ERROR: That is not a valid selection, try again."
SPACER_SIZE = 20
foodMenu  = { 1: (Tacos, 1), 2: (Burrito, 4), 3: (Soda, 1.5), 5: (Water, 1.0) }

# displays Home Page of the Point Of Sale (POS) module
def displayPOSMenuHome():
    validMenuChoice = False

    while not validMenuChoice:
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
        if menuChoice == 1:
            validMenuChoice = True
            displayMakeSaleMenu()
        elif menuChoice == 2: # modify sale
            validMenuChoice = True
            displayModifySaleMenu()
        else: # default case
            print(ERROR_PROMPT)

    mainMenu.mainMenu()  # return to home menu


# displays the POS menu page
def displayPosMenu():
    validMenuChoice = False
    menuSelection = 1

    while not validMenuChoice:
        # print the POS menu and take initial input
        itemNumSearch = input( "Enter the sale item number to view (A for all): " )

        # check if itemNumSearch is for char for VIEW ALL
        try:
            if str.upper(itemNumSerach) == 'A':
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

        # take user input on newline
        menuChoice = input("")
        
        try:
            menuChoice = int(menuChoice)
        except ValueError as err:
            print(ERROR_PROMPT, " at displayPOSMenu() ", err)

        # now check if int is within appropriate range
        if int(menuChoice = True # passed all tests and exits loop

        # input passes all test; search line items and print result
        if int(menuChoice) == 1:
               if makeSale():
                   print("Item selected successfully")
               else: # default case
                   print("Error adding item! Did not complete.")

        elif int(menuChoice) == 2:
               if modifySale():
                   print("Sale modified successfully!")
               else: # default case
                   print("Error modifying sale! Did not complete.")

        elif int(menuChoice) == 0:
               return True # user wants to return to the main menu

        # error case, should not hit during normal execution
        else:
               displayPOSMenuHome()



def searchSales(lineItemNum):
        # searches database for record matching lineItemNum
        # returns Sales instance matching the lineItemNum or blank
        if salesSQL.searchForSQLRecord(lineItemNum):
            return salesSQL.creatSalesFromSQLRecord(lineItemNum)

        return None

