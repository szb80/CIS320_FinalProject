# CIS320 Final Project
# Hugo & Seth
# SB 4/20

# Imports
import InventoryModule, Inventory, sqlite3

# Initialize variables

# Global static for total modules available in program
# Adjust the MAX_MODULES variable when adding additional modules to program.
MAX_MODULES = 3

menuChoice = 0  # initialize out of scope before prompting user for input


# validates if the menu choice was within the appropriate range
def validateMenuChoice(num):
    return num in range(1, MAX_MODULES + 1)


# displays the main menu
# accepts the managerFlag boolean to determine menu display
def mainMenu(managerFlag):
    # main menu loop, display menu until valid selection is made
    while not validateMenuChoice(menuChoice):
        # print the menu
        print("MAIN MENU", "-" * 20)
        print("1) Inventory")
        if managerFlag:  # only for the bosses!
            print("2) Personnel")
            print("3) POS")
        else:  # sorry, just an employee
            print("3) POS")

        # take the user menu choice
        # validate the input as an int and catch exceptions
        try:
            menuChoice = int(input())
        except ValueError:
            print("Incorrect selection, try again!")


    # call module menus
    if menuChoice == 1:
        InventoryModule.displayInventoryMenu()
    elif menuChoice == 2:
        if managerFlag:
            # displayPersonnelMenu()
            print()
        else:
            print("You do not have the appropriate permissions.")
    elif menuChoice == 3:
        print()
        # displayPOSMenu()
    else:
        menuChoice == 0  # invalid menu choice, default to 0


# main(), 'nuff said
def main():

    # userLogin()
    # setManagerFlag()

    managerFlag = True

    #mainMenu(managerFlag)





    ############################################################################
    # SQLITE TESTING
    ############################################################################

    flour = Inventory.Inventory()
    flour.setItemNumber(100)
    flour.setItemName("Flour")
    flour.setItemDesc("Whole wheat flour cracked")
    flour.setStockCount(99)



    conn = sqlite3.connect('inventory.db')
    table_name = 'inventory_db'
    c = conn.cursor()





    # create new record -------------------------------------------
    # WORKING!
    try:
        c.execute("INSERT INTO inventory_db VALUES(?, ?, ?, ?)"
                  , (flour.getItemNumber()
                     , flour.getItemName()
                     , flour.getItemDesc()
                     , flour.getStockCount()
                     )
                  )
    except sqlite3.IntegrityError:
        print("ERROR: ID already exists!")

    # ------------------------------------------------------------


    # search for a matching SQL record: --------------------------
    c.execute(
        '''SELECT * FROM inventory_db WHERE itemNumber=?'''
        , (flour.getItemNumber(),)
    )
    record = c.fetchone()

    # print(record)  # must translate into Invenotry object

    # ------------------------------------------------------------


    # update an existing record ----------------------------------
    # WORKING
    try:
        c.execute(
            "UPDATE inventory_db SET itemName=?, itemDesc=?, stockCount=? WHERE itemNumber=?"
            , (flour.getItemName()
               , flour.getItemDesc()
               , flour.getStockCount()
               , flour.getItemNumber()
               )
            )

    except sqlite3.IntegrityError:
        print("ERROR: ID doesn't exist!")

    # ------------------------------------------------------------





    conn.commit()
    conn.close()






main()