# CIS320 Final Project
# Gustavo, Hugo & Seth
# SB 4/23

import Validate, Inventory, InventorySQL

ERROR_PROMPT = "**ERROR: That is not a valid selection, try again."


# displays the home page of the Inventory module menu
def displayInventoryMenuHome():  # ++++++++++++++++++++++++++++++++++++++++++++
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
def displayCheckInventoryMenu():  # +++++++++++++++++++++++++++++++++++++++++++
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


def displayModifyInventoryMenu():  #+++++++++++++++++++++++++++++++++++++++++++
    # displays the Modify Inventory menu
    validMenuChoice = False  # sentinel for menu display loop
    menuChoice = 0  # initialize to 0

    while not validMenuChoice:
        # print the options
        print("(1)  Add Inventory Item")
        print("(2)  Modify Inventory Item")
        print("(3)  Delete Inventory Item")

        # take user input
        menuChoice = input("")

        # check if an int, else throw error and catch exception
        try:
            menuSelection = int(menuChoice)  # attempt cast to int
        except ValueError as err:
            print(ERROR_PROMPT, " at displayCheckInventoryMenu() ", err)

        # now check if int is within appropriate range
        if int(menuChoice) >= 1 or int(menuChoice) <= 3:
            validMenuChoice = True  # passes all tests and exits loop

    # input passes all tests; run search and print result
    if int(menuChoice) == 1:
        addInventoryItem()
    elif int(menuChoice) == 2:
        modifyInventoryItem()
    elif int(menuChoice) == 3:
        deleteInventoryItem()
    else:
        displayModifyInventoryMenu()  # error case, should not display

    return True


def searchInventory(itemNum):
    # searches database for record matching itemNum
    # returns Inventory instance matching itemNum or blank

    if InventorySQL.searchForSQLRecord(itemNum):
        return InventorySQL.createInventoryFromSQLRecord(itemNum)

    return None


def displayAllInventory():
    # displays all inventory in the database

    # create list of all inventory in DB



    # call displayInventory() on each record number



    return True


def addInventoryItem():  # +++++++++++++++++++++++++++++++++++++++++++++++++++++
    # adds a new inventory item
    isValid = False
    Validate.cls()  # clear screen

    print("ADDING NEW ITEM:", "-" * 20)

    while not isValid:
        newItemNum = input("Enter an ID: ")
        # check if ID is a number and loop until valid
        if not Validate.validateInt(newItemNum):
            print("**ERROR: must be a number.")
        # check if ID is in database already and loop until valid
        if InventorySQL.searchForSQLRecord(newItemNum):
            print("**ERROR: ID already exists.")

        # check if both criteria are met and exit loop
        if not InventorySQL.searchForSQLRecord(newItemNum) \
                and Validate.validateInt(newItemNum):
            isValid = True

    newName = str(input("Enter the name: "))  # take name
    newDesc = str(input("Enter the description: "))  # take description

    newStock = input("Enter the stock count: ")  # take stock count
    while not Validate.validateFloat(newStock): # validate is number
        newStock = input("**ERROR: must be as number. Enter the stock count: ")

    # all variables now populated and validated

    # make an object
    newInventory = Inventory.Inventory(newItemNum, newName, newDesc, newStock)
    # attempt write and return status
    return InventorySQL.createSQLRecord(newInventory)


def modifyInventoryItem():  # +++++++++++++++++++++++++++++++++++++++++++++++++
    # modifies an existing inventory item
    isValid = False
    Validate.cls()  # clear screen

    # take an item number to modify and loop until valid
    while not isValid:
        newItemNum = input("Enter an ID to modify: ")
        # check if ID is a number and loop until valid
        if not Validate.validateInt(newItemNum):
            print("**ERROR: must be a number.")
        # check if ID is in database already and loop until valid
        if not InventorySQL.searchForSQLRecord(newItemNum):
            print("**ERROR: ID does not exist.")

        # check if both criteria are met and exit loop
        if InventorySQL.searchForSQLRecord(newItemNum) \
                and Validate.validateInt(newItemNum):
            isValid = True

    # take updated name and desc strings
    newName = str(input("Enter the updated name: [enter for no change] "))
    newDesc = str(input("Enter the updated description: [enter for no change] "))

    # take updated stock count value
    newStock = input("Enter the stock count: [0 for no change] ")
    while not Validate.validateFloatOrEmpty(newStock): # validate is number
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

    # make an object
    newInventory = Inventory.Inventory(newItemNum, newName, newDesc, newStock)
    # attempt write and return status
    return InventorySQL.updateSQLRecord(newInventory)


def deleteInventoryItem(): # ++++++++++++++++++++++++++++++++++++++++++++++++++
    # deletes an existing inventory record
    isValid = False

    # loop menu until valid input is entered
    while not isValid:
        itemID = input("Enter the ID to delete: ")
        # check if ID is a number and loop until valid
        if not Validate.validateInt(itemID):
            print("**ERROR: must be a number.")
            continue
        # check if ID is not in database already and loop until valid
        if not InventorySQL.searchForSQLRecord(itemID):
            print("**ERROR: ID does not exist.")

        # check if both criteria are met and exit loop
        if InventorySQL.searchForSQLRecord(itemID) \
                and Validate.validateInt(itemID):
            isValid = True

    return InventorySQL.deleteSQLRecord(itemID)


