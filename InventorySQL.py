# CIS320 Final Project
# Gustavo, Hugo & Seth
# SB 4/25

import Inventory, sqlite3


def displayTable():
    # displays all records from the database
    # returns boolean for successful
    # + creates connection to database

    # search for record to delete
    try:
        # connect to database
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        conn.execute('''SELECT * FROM inventory_db''')
        print("executed SELECT")##############################################
        all_rows = c.fetchone()
        print("executed fetchall()")  #######################################

        print("All_rows literal: ", all_rows)  ################################

        #for row in all_rows:
            #print("Printing for loop")
            #print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
            #print("ItemID ", row, ": ", row[0], "Name: ", row[1])

        # commit and execute
        conn.close()

        return True

    except sqlite3.IntegrityError as err:
        print("**ERROR: at deleteSQLRecord()", err)

    return False




def createSQLRecord(inventoryItem): # +++++++++++++++++++++++++++++++++++++++++
    # creates a new SQL record for a non-existing itemNumber
    # returns boolean for successful record creation
    # + creates connection to database

    # setup database connection
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    success = False  # initial return condition

    try:
        # try to execute insert record command on c
        c.execute("INSERT INTO inventory_db VALUES(?, ?, ?, ?)"
                  , (inventoryItem.getItemNumber()
                     , inventoryItem.getItemName()
                     , inventoryItem.getItemDesc()
                     , inventoryItem.getStockCount()
                     )
                  )
        success = True  # successful creation of record

    except sqlite3.IntegrityError as err:
        print("ERROR: itemID already exists!  createSQLRecord()", err)

    # write and close db
    conn.commit()
    conn.close()

    return success


def updateSQLRecord(inventoryItem): # ++++++++++++++++++++++++++++++++++++++++++
    # updates an existing SQL record
    # returns boolean for record updated successfully
    # + creates connection to database

    # setup database connection
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    success = False  # initial return condition

    try:
        # try to execute update matching record command on c
        c.execute(
            "UPDATE inventory_db SET itemName=?, itemDesc=?, stockCount=? WHERE itemNumber=?"
            , (inventoryItem.getItemName()
               , inventoryItem.getItemDesc()
               , inventoryItem.getStockCount()
               , inventoryItem.getItemNumber()
               )
        )
        success = True  # successful update record

    except sqlite3.IntegrityError as err:
        print("ERROR: itemID doesn't exist!  updateSQLRecord()", err)

    # write and close DB
    conn.commit()
    conn.close()

    return success


def searchForSQLRecord(itemID):  # ++++++++++++++++++++++++++++++++++++++++++++
    # searches the database for a matching record to the passed itemID
    # returns a boolean for record is found
    # + creates connection to database

    # connect to database
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()

    # select record
    c.execute(
      '''SELECT * FROM inventory_db WHERE itemNumber=?'''
      , (itemID,)
    )
    idExists = c.fetchone()

    conn.close()  # close DB connection without commit

    if idExists:  # record was found in DB
        return True
    else:
        return False


def createInventoryFromSQLRecord(itemID):  # ++++++++++++++++++++++++++++++++++
    # takes a passed itemID and creates an Inventory instance
    # with the data returned from the record
    # returns Inventory instance for matching itemID
    # + creates connection to database

    if searchForSQLRecord(itemID):  # record exists
        # connect to database
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()

        # select row from
        c.execute(
            '''SELECT * FROM inventory_db WHERE itemNumber=?'''
            , (itemID,))
        idExists = c.fetchone()

        # close connection without commit
        conn.close()

        # build Inventory instance to return with 4 columns
        return Inventory.Inventory(idExists[0]
                                   , idExists[1]
                                   , idExists[2]
                                   , idExists[3]
                                   )

    else:
        return None


def deleteSQLRecord(itemID):  # +++++++++++++++++++++++++++++++++++++++++++++++
    # drops a record from the database
    # returns boolean for successful
    # + creates connection to database

    # search for record to delete
    if searchForSQLRecord(itemID):
        try:
            # connect to database
            conn = sqlite3.connect('inventory.db')
            c = conn.cursor()
            conn.execute('''DELETE from inventory_db where itemNumber = ?'''
                         , (itemID,))

            # commit and execute
            conn.commit()
            conn.close()

            return True

        except sqlite3.IntegrityError as err:
            print("**ERROR: at deleteSQLRecord()", err)

    return False
