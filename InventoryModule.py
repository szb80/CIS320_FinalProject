# CIS320 Final Project
# Gustavo, Hugo & Seth
# SB 4/23

import Validate, Inventory, InventorySQL, mainMenu

# GLOBAL CONSTANTS
ERROR_PROMPT = "**ERROR: That is not a valid selection, try again."
SPACER_SIZE = 20


def displayInventoryMenuHome(managerFlag):  # tested
    # displays the home page of the Inventory module menu
    # SB

    exitMenu = False

    # loop through invalid input for menu display
    while not exitMenu:
        #Validate.cls()  # clear screen before run
        # print the menu
        print("INVENTORY MENU", "=" * SPACER_SIZE)
        print("(1)  Check Inventory")
        print("(2)  Modify Inventory")
        print("(0)  < Go Back")

        # take user menu choice
        try:
            menuChoice = int(input())
        except ValueError:
            print(ERROR_PROMPT)
            continue

        # call sub modules
        if menuChoice == 1:  # check inventory
            displayCheckInventoryMenu()
        elif menuChoice == 2:  # modify inventory
            displayModifyInventoryMenu()
        elif menuChoice == 0:  # return up one level
            exitMenu = True
            return True  # exit function and return to calling menu
        else:  # default case
            print(ERROR_PROMPT)

    return False


def displayCheckInventoryMenu():  # tested
    # displays the Check Inventory menu page
    # SB

    exitFlag, validMenuChoice = False, False
    menuSelection = 1  # initialize display all sentinel

    #Validate.cls()  # clear screen

    while not exitFlag:
        while not validMenuChoice:
            # print the menu and take initial input
            itemNumSearch = input("Enter the item number to view (A for all): ")

            # check if itemNumSearch is char for VIEW ALL
            try:
                if str.upper(itemNumSearch) == 'A':
                    menuSelection = 0  # sentinel for display all
                    validMenuChoice = True  # exit loop and display menu
                    continue
            except ValueError:
                # catch error but continue
                print()

            # check if if itemNumSearch is an int, else throw error
            try:
                itemNumSearch = int(itemNumSearch)  # attempt cast to int
            except ValueError as err:
                print(ERROR_PROMPT)
                continue

            # menu choice is an int and not ALL, user must want to check item number
            # now check if int is within appropriate range
            inventorySizeParams = Inventory.Inventory()  # create instance to call
            if int(inventorySizeParams.MIN_ITEM_NUMBER_SIZE) \
                    <= itemNumSearch \
                    <= int(inventorySizeParams.MAX_ITEM_NUMBER_SIZE):
                validMenuChoice = True  # passes all tests and exits loop

        # input passes all tests; run search and print result
        if validMenuChoice:
            if menuSelection == 0:  # sentinel set to display all
                displayAllInventory()
                exitFlag = True
                return True
            else:
                # search for record
                if searchInventory(itemNumSearch) is None:  # record does not exist
                    print("Item not found in inventory.")  # notify and exit
                    exitFlag = True
                    return False
                else:
                    # record found, print it and exit
                    InventorySQL.displayRecord(itemNumSearch)
                    exitFlag = True
                    return True
        else:  # error case
            print(ERROR_PROMPT)
            exitFlag = True

    return False  # return to Inventory home menu


def displayModifyInventoryMenu():  # tested
    # displays the Modify Inventory menu
    # SB

    exitFlag = False  # sentinel for menu display loop
    menuChoice = -1  # initialize to -1 as sentinel

    #Validate.cls()  # clear screen

    print("MODIFY INVENTORY ", "-" * SPACER_SIZE)

    while not exitFlag:
        # print the options
        print("(1)  Add Inventory Item")
        print("(2)  Modify Inventory Item")
        print("(3)  Delete Inventory Item")
        print("(0)  < Go Back")

        # take user input on newline
        menuChoice = input("")

        # check if an int, else throw error and catch exception
        try:
            menuChoice = int(menuChoice)  # attempt cast to int
        except ValueError as err:
            print(ERROR_PROMPT, " at displayCheckInventoryMenu() ", err)

        # now check if int is within appropriate range
        if int(menuChoice) >= 0 or int(menuChoice) <= 3:
            exitFlag = True  # passes all tests and exits loop

        # input passes all tests; run search and print result
        if int(menuChoice) == 1:
            if addInventoryItem():
                print("Item added successfully!")
            else:  # default case
                print("Error adding item!  Did not complete.")

        elif int(menuChoice) == 2:
            if modifyInventoryItem():
                print("Item modified successfully!")
            else:  # default case
                print("Error modifying item!  Did not complete.")

        elif int(menuChoice) == 3:
            if deleteInventoryItem():
                print("Record deleted successfully!")
            else:  # default case
                print("Nothing was deleted.")

        elif int(menuChoice) == 0:
            return True  # user wants to quit, exit function and return to caller

        # error case, should not hit during normal execution
        else:
            displayModifyInventoryMenu()

    # return to Inventory home menu
    return True


def searchInventory(itemNum):  # tested
    # searches database for record matching itemNum
    # returns Inventory instance matching itemNum or blank
    # SB

    if InventorySQL.searchForSQLRecord(itemNum):
        return InventorySQL.createInventoryFromSQLRecord(itemNum)

    return None


def displayAllInventory():  # tested
    # displays all the inventory records in the database
    # SB
    return InventorySQL.displayTable()


def addInventoryItem():  # tested
    # adds a new inventory item
    # SB

    isValid = False  # initialize menu sentinel

    #Validate.cls()  # clear screen

    print("ADDING NEW RECORD ", "-" * SPACER_SIZE)

    # start menu loop
    while not isValid:
        newItemNum = input("Enter an ID: ")
        # check if ID is a number and loop until valid
        if not Validate.validateInt(newItemNum):
            print("**ERROR: must be a number.")
            continue
        # check if ID is in database already and loop until valid
        if InventorySQL.searchForSQLRecord(newItemNum):
            print("**ERROR: ID already exists.")
            continue

        # check if both criteria are met and exit loop
        if not InventorySQL.searchForSQLRecord(newItemNum) \
                and Validate.validateInt(newItemNum):
            isValid = True

    # begin taking input for item:
    newName = str(input("Enter the name: "))  # take name

    newDesc = str(input("Enter the description: "))  # take description

    newStock = input("Enter the stock count: ")  # take stock count
    while not Validate.validateFloat(newStock): # validate is number
        newStock = input("**ERROR: must be as number. Enter the stock count: ")

    # all variables are now populated and validated

    # make an Inventory object instance
    newInventory = Inventory.Inventory(newItemNum, newName, newDesc, newStock)

    # attempt write and return status
    return InventorySQL.createSQLRecord(newInventory)


def modifyInventoryItem():  # tested
    # modifies an existing inventory item
    # SB

    isValid = False

    #Validate.cls()  # clear screen

    print("MODIFYING RECORD ", "-" * SPACER_SIZE)

    # take an item number to modify and loop until valid
    while not isValid:
        newItemNum = input("Enter an ID to modify: ")
        # check if ID is a number and loop until valid
        if not Validate.validateInt(newItemNum):
            print("**ERROR: must be a number.")
            continue  # reset loop to top
        # check if ID is in database already and loop until valid
        if not InventorySQL.searchForSQLRecord(newItemNum):
            print("**ERROR: ID does not exist.")
            continue  # reset loop to top

        # check if both criteria are met and exit loop
        if InventorySQL.searchForSQLRecord(newItemNum) \
                and Validate.validateInt(newItemNum):
            isValid = True

    # print copy of current record in db
    print("Current Record:\n")
    InventorySQL.displayRecord(newItemNum)

    # take updated name and desc strings
    newName = str(input("Enter the updated name: [enter for no change] "))
    newDesc = str(input("Enter the updated description: [enter for no change] "))

    # take updated stock count value
    newStock = input("Enter the stock count: [0 for no change] ")
    while not Validate.validateFloatOrEmpty(newStock) \
            or Validate.validateFloatOrEmpty(newStock) >= 0: # validate is > 0
        newStock = input("**ERROR: must be as number. Enter the stock count: ")

    # all variables are now populated and validated

    # create oldInventory instance with current values in DB
    oldInventory = Inventory.Inventory(
        InventorySQL.createInventoryFromSQLRecord(newItemNum).getItemNumber()
        , InventorySQL.createInventoryFromSQLRecord(newItemNum).getItemName()
        , InventorySQL.createInventoryFromSQLRecord(newItemNum).getItemDesc()
        , InventorySQL.createInventoryFromSQLRecord(newItemNum).getStockCount()
    )

    # if the user entered a blank string for variable, keep current values
    if newName == "":
        newName = oldInventory.getItemName()
    if newDesc == "":
        newDesc = oldInventory.getItemDesc()
    if newStock == "":
        newStock = oldInventory.getStockCount()

    # make an object instance
    newInventory = Inventory.Inventory(newItemNum, newName, newDesc, newStock)
    # attempt write and return status
    return InventorySQL.updateSQLRecord(newInventory)


def deleteInventoryItem(): # tested
    # deletes an existing inventory record
    # SB

    isValid = False

    #Validate.cls()  # clear screen

    print("DELETING RECORD ", "-" * SPACER_SIZE)

    # loop menu until valid input is entered
    while not isValid:
        itemID = input("Enter the ID to delete: [0 to cancel] ")
        # check if ID is a number and loop until valid
        if not Validate.validateInt(itemID):
            print("**ERROR: must be a number.")
            continue
        if int(itemID) == 0:
            return False
        # check if ID is not in database already and loop until valid
        if not InventorySQL.searchForSQLRecord(itemID):
            print("**ERROR: ID does not exist.")

        # check if both criteria are met and exit loop
        if InventorySQL.searchForSQLRecord(itemID) \
                and Validate.validateInt(itemID):
            isValid = True

    return InventorySQL.deleteSQLRecord(itemID)
