# CIS320 Final Project
# Gustavo, Hugo & Seth
# SB 4/25

# InventorySQL class
# Contains methods for accessing the SQL database

import Inventory, sqlite3


def displayRecord(itemID): # ++++++++++++++++++++++++++++++++++++++++++++++++++
    # displays a single record from the database
    # returns boolean for successful
    # + creates connection to database

    # search for record to delete
    try:
        # connect to database
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()

        # select record
        c.execute(
            '''SELECT * FROM inventory_db WHERE itemNumber=?'''
            , (itemID,)
        )
        idExists = c.fetchone()  # load record into variable

        # print record formatted
        print('Item ID:\t\t{0}\nName:\t\t\t{1}\nDescription:\t{2}\nStock:\t\t\t{3}\n'.format(idExists[0], idExists[1], idExists[2], idExists[3]))

        # close the file and return successful
        conn.close()
        return True

    # catch any errors and return false
    except sqlite3 as err:
        print("**ERROR: at displayRecord()", err)
    return False


def displayTable(): #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # displays all records from the database
    # returns boolean for successful
    # + creates connection to database

    # search for record to delete
    try:
        # connect to database
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()

        # select all rows
        c.execute('''SELECT * FROM inventory_db''', ())
        result = c.fetchall()

        for row in result:
            print('Item ID:\t\t{0}\nName:\t\t\t{1}\nDescription:\t{2}\nStock:\t\t\t{3}\n'.format(row[0], row[1], row[2], row[3]))

        # close the file
        conn.close()

        return True

    # catch any errors in the file
    except sqlite3 as err:
        print("**ERROR: at displsayTable()", err)
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
            conn.execute('''DELETE from inventory_db where itemNumber=?'''
                         , (itemID,))

            # commit and execute
            conn.commit()
            conn.close()

            return True

        except sqlite3.IntegrityError as err:
            print("**ERROR: at deleteSQLRecord()", err)

    return False
