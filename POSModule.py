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


def displayPOSMenuHome(): # tested
    # displays Home Page of the Point Of Sale (POS) module
    exitFlag = False  # menu sentinel

    while not exitFlag:
        #print POS menu
        print("POS MENU", "=" * SPACER_SIZE)
        print("(1)  Make Sale")
        print("(2)  Modify Sale")
        print("(0)  Return")

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

    mainMenu.mainMenu()  # return to home menu


def displayMakeSaleMenu(): # tested
    # creates a new sale to write to database

    # set a timestamp that will become the sale number for use
    # throughout the rest of the transaction
    saleNumber = int(str(datetime.datetime.utcnow().timestamp()).split(".")[0])
    exitFlag, invalid = False, True  # loop sentinel for menus
    selection, quantity = -1, 0  # initialize out of range

    # display sale menu
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

    if not exitFlag:
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

    displayPOSMenuHome()  # return to home menu, sale completed


def displayModifySaleMenu(): # -----------------------------------------------
    # displays the modify sale submenu
    exitFlag = False
    saleNumber = 1
    menuChoice = -1

    print("MODIFY SALE", "-" * SPACER_SIZE)  # display header

    # get a valid sale to modify
    while not SaleSQL.searchForSQLRecord(saleNumber):
        print("Enter the sale number to modify or (0) to exit: ")
        try:
            saleNumber = int(input())
        except ValueError:
            print("**ERROR: Enter a valid number!")
            continue
        if int(saleNumber) == 0:
            exitFlag = True
            break  # abort early and skip rest of function
        print("**ERROR: Sale does not exist!")  # error case

    # DISPLAY MODIFY SUBMENU OPTIONS
    while not exitFlag:
        # display primary menu options after successful
        print("(1)  Adjust Quantity")
        print("(2)  Refund Item")

        try:
            menuChoice = int(input())
        except ValueError:
            print("**ERROR: Must be a number!")

        if int(menuChoice) == 1:
            if modifySaleLineItemQty(saleNumber):
                print("Updated successfully!")
            else:
                print("**ERROR: Failed to update!")
        elif int(menuChoice) == 2:
            if refundSaleLineItem(saleNumber):
                print("Updated Successfully!")
            else:
                print("**ERROR: Failed to update!")
        else:  # error case
            print(ERROR_PROMPT)
            continue  # back to top of modify submenu, out of range

    return True


def modifySaleLineItemQty(saleNum):
    # adjusts the quantity of a sale item
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
                      , "\t\t$"
                      , "{:.02f}".format(v[1])
                      , "\t\t"
                      , v[0]
                      , sep="")

            # take the user input
            try:
                menuItem = int(input())
            except ValueError:
                print(ERROR_PROMPT)

            # validate within menu range
            if menuItem in range(0, len(foodMenu) + 1):
                # see if this item was sold in this sale
                for k,v in foodMenu.items():
                    if



    else:
        return False  # sale not found in database!  error case



# def modifySaleLineItemQty():
#     # adjsuts sale item quantity
#     isValid = False  # initialize menu sentinel
#
#     print("Adjusted item quantity", "-" * SPACER_SIZE)
#
#     # start menu loop
#     while not isValid:
#         lineItemQty = input("Enter the quantity of the item you want to order: ")
#         # check if quantity is available and loop until valid
#         if not Validate.validateInt(lineItemQty):
#             print("**ERROR: select valid amount.")
#             continue
#
#         # check if both criteria are met and exit loop
#         if not SaleSQL.searchForSQLRecord(lineItemQty) \
#                 and Validate.validateInt(lineItemQty):
#             isValid = True
#
#     # begin taking input for item:
#     lineItemNum = str("Enter the item you wish to purchase: ") # take name of item
#
#     lineItemQty = str("Enter the quantity: ") # take the amount of the item
#
#     # make a new sale record
#     newSaleNumber = SaleSQL.createSQLRecord(newSaleNumber) ##### NOT SURE HOW TO COMPLETE THIS RECORD!!!
#
#     # attempt write and return status
#     return SaleSQL.createSQLRecord(newSaleNumber)



def deleteSaleNumber():
    # deletes an existing order
    isValid = False

    # Validates.cls()

    print("DELETING ORDER ", "-" * SPACER_SIZE)

    # loop menu until valid input is entered
    while not isValid:
        saleNumber = input("Enter the sale number to delete: [0 to cancel] " )
        # check if saleNumber is a number and loop until valid
        if not Validate.validateInt(saleNum):O
        print("**ERROR: must be a number.")
        continue
    if int(saleNum) == 0:
        return False
    # check if sale number is still in database and loop until valid
    if SaleSQL.searchForSQLRecord(saleNum) \
            and Validate.validateInt(saleNum):
        isValid = True

    return SaleSQL.deleteSQLRecord(saleNum)

