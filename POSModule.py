# CIS320 Final Project POS
# Gustavo, Hugo & Seth
# GC 5/12, SB 5/15

import Validate, Sale, SaleSQL, mainMenu, datetime

# global constants
ERROR_PROMPT = "**ERROR: That is not a valid selection, try again."
SPACER_SIZE = 20

# initialize menu dictionary
foodMenu  = { 1: ("Taco", 1)
    , 2: ("Burrito", 4)
    , 3: ("Soda", 1.5)
    , 4: ("Water", 1.0)
              }


def displayPOSMenuHome(managerFlag): # tested
    # displays Home Page of the Point Of Sale (POS) module
    # GC

    exitFlag = False  # menu sentinel

    while not exitFlag:
        #Validate.cls()

        #print POS menu
        print("POS MENU", "=" * SPACER_SIZE)
        print("(1)  Make Sale")
        print("(2)  Modify Sale")
        print("(0)  < Go Back")

        # take user menu choice
        try:
            menuChoice = int(input())
        except ValueError:
            print(ERROR_PROMPT)
            continue  # reset loop to top

        # Call sub modules
        if int(menuChoice) == 1:  # make a sale
            displayMakeSaleMenu()
        elif int(menuChoice) == 2:  # modify sale
            displayModifySaleMenu()
        elif int(menuChoice) == 0:  # exit case
            exitFlag = True
        else: # default case
            print(ERROR_PROMPT)

    return True  # exit and return to home menu


def displayMakeSaleMenu(): # tested
    # creates a new sale to write to database
    # GC, SB

    # set a timestamp that will become the sale number for use
    # throughout the rest of the transaction
    saleNumber = int(str(datetime.datetime.utcnow().timestamp()).split(".")[0])
    exitFlag, invalid = False, True  # loop sentinel for menus
    selection, quantity = -1, 0  # initialize out of range

    # display sale menu
    #Validate.cls()
    print("MAKE SALE", "-" * SPACER_SIZE)
    while not exitFlag:
        # show the menu options
        print("Add to sale or (0) to exit:")
        for k, v in foodMenu.items():
            print("\t"
                  , k
                  , "\t\t$"
                  , "{:.02f}".format(v[1])
                  , "\t\t"
                  , v[0]
                  , sep="")

        try:
            selection = int(input(""))
        except ValueError:
            print("**ERROR: Not a number!")
            continue  # return to top of loop and try again

        if selection == 0:
            exitFlag = True

        elif selection not in foodMenu.keys():
            print("**ERROR: Not a valid selection!")
            continue  # reset to top

        else:  # passed menu selection validation, continue to next step
            while invalid:  # quantity validation loop
                print("Enter the Quantity: ")
                try:
                    quantity = int(input())
                except ValueError:
                    print("**ERROR: Not a number!")
                    continue
                if quantity > 0:
                    break  # valid quantity, continue to next step
                else:  # error case, catch everything else
                    continue  # and return to top of quantity loop

            # all validations passed and data collected
            # create Sale instance with validated data
            lineItem = Sale.Sale(saleNumber, selection, quantity)

            # attempt write to database
            if SaleSQL.createSQLRecord(lineItem):
                print("Success!")
            else:  # error case, should not occur
                print("**ERROR: Purchase item not saved to database!")

    if exitFlag:
        #Validate.cls()
        # sale process completed, proceed with finalization
        totalPrice = 0

        for k,v in foodMenu.items():
            if SaleSQL.searchForSQLRecord(saleNumber):  # sale exists, continue
                # add to total price the quantity times the cost
                totalPrice += SaleSQL.returnSaleQuantity(saleNumber, k) * v[1]

        print("TOTAL:"
            , "." * SPACER_SIZE
            , "$"
            , "{:.02f}".format(totalPrice)
            , sep="")

        input("Press <ENTER> to confirm sale")

    return True  # return to home menu, sale completed


def displayModifySaleMenu(): # tested
    # displays the modify sale submenu
    # GC, SB

    exitFlag = False
    saleNumber = 1
    menuChoice = -1

    #Validate.cls()  # clear the screen
    print("MODIFY SALE", "-" * SPACER_SIZE)  # display header

    # get a valid sale to modify
    while not SaleSQL.searchForSQLRecord(saleNumber):
        print("Enter the sale number to modify or (0) to exit: ")
        try:  # take input and loop until valid
            saleNumber = int(input())
        except ValueError:
            print("**ERROR: Enter a valid number!")
            continue
        if int(saleNumber) == 0:
            exitFlag = True
            return False  # abort early and skip rest of function
        elif not SaleSQL.searchForSQLRecord(saleNumber):
            print("**ERROR: Sale not found!")
            continue

    # DISPLAY MODIFY SUBMENU OPTIONS
    while not exitFlag:
        #Validate.cls()
        # display submenu options
        print("(1)  Adjust Quantity")
        print("(2)  Refund Item")
        print("(0)  ..\ Up One Level")

        try:
            menuChoice = int(input())
        except ValueError:
            print("**ERROR: Must be a number!")

        if int(menuChoice) == 1:  # option 1 - modify quantity
            if modifySaleLineItemQty(saleNumber):
                print("Updated successfully!")
            else:
                print("**ERROR: Failed to update quantity!")
            exitFlag = True  # exit loop

        elif int(menuChoice) == 2:  # option 2 - refund sale
            if refundSaleLineItem(saleNumber):
                print("Refunded Successfully!")
            else:
                print("**ERROR: Failed to refund item!")
            exitFlag = True  # exit loop

        elif int(menuChoice) == 0:  # exit choice
            exitFlag = True  # exit loop

        else:  # error case
            print(ERROR_PROMPT)
            continue  # back to top of modify submenu, out of range

    return True


def modifySaleLineItemQty(saleNum):  # tested
    # adjusts the quantity of a sale item
    # SB

    # initialize variables
    menuItem, newQty = 0, 0
    menuFlag, found = False, False

    if SaleSQL.searchForSQLRecord(saleNum):
        # sale exists, proceed with function
        while not menuFlag:
            print("Enter the menu number to modify: ")
            # show the menu options
            for k, v in foodMenu.items():
                print("\t"
                      , k
                      , "\t\t"
                      , v[0]
                      , sep="")

            # take the user input and loop until valid
            try:
                menuItem = int(input())
            except ValueError:
                print(ERROR_PROMPT)
                continue

            # validate input is within menu range
            # and a valid menu choice
            if menuItem in range(0, len(foodMenu) + 1):
                # see if this item was sold in this sale
                for k,v in foodMenu.items():
                    if menuItem == k:
                        # item was present in sale, input the modified quantity
                        print("Enter the updated quantity: ")
                        newQty = input()

                        # loop until good input is found
                        while not Validate.validateInt(newQty):
                            print("**ERROR: Enter a valid number!")
                            newQty = input()

                        # we now have a valid sale, menu item, and new quantity
                        # write it to the database now

                        if SaleSQL.updateSQLRecordQty(saleNum, menuItem, newQty):
                            menuFlag = True  # successfully written to DB

    return menuFlag  # return status of menu run


def refundSaleLineItem(saleNumber):
    # refunds a sale line item for a specific menu choice
    # SB

    # initialize variables
    menuItem, newQty = 0, 0
    menuFlag, found = False, False

    #Validate.cls()

    print("REFUND LINE ITEM ", "-" * SPACER_SIZE)

    if SaleSQL.searchForSQLRecord(saleNumber):
        # if sale exists, proceed with function
        while not menuFlag:
            print("Enter the menu number to refund: ")
            # show the menu options
            for k, v in foodMenu.items():
                print("\t"
                      , k
                      , "\t\t"
                      , v[0]
                      , sep="")

            # take the user input and loop until valid
            try:
                menuItem = int(input())
            except ValueError:
                print(ERROR_PROMPT)
                continue

            # validate input is within menu range
            # and a valid menu choice
            if menuItem in range(0, len(foodMenu) + 1):
                # see if this item was sold in this sale
                for k,v in foodMenu.items():
                    if menuItem == k:
                        # item was present in sale, set quantity to 0
                        if SaleSQL.updateSQLRecordQty(saleNumber
                                , menuItem
                                , 0):
                            menuFlag = True  # successfully written to DB

    return menuFlag  # return status of menu run
