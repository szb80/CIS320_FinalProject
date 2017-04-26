# CIS320 Final Project
# Gustavo, Hugo & Seth
# SB 4/25

import Inventory, sqlite3


def createSQLRecord(inventoryItem):
    # creates a new SQL record for a non-existing itemNumber
    # setup database connection
    conn = sqlite3.connect('inventory.db')
    table_name = 'inventory_db'
    c = conn.cursor()
    success = False

    try:
        # try to execute insert record command on c
        c.execute("INSERT INTO inventory_db VALUES(?, ?, ?, ?)"
                  , (inventoryItem.getItemNumber()
                     , inventoryItem.getItemName()
                     , inventoryItem.getItemDesc()
                     , inventoryItem.getStockCount()
                     )
                  )
        success = True

    except sqlite3.IntegrityError:
        print("ERROR: itemID already exists!")

    # write and close db
    conn.commit()
    conn.close()

    return success


def updateSQLRecord(inventoryItem):
    # updates an existing SQL record
    # setup database connection
    conn = sqlite3.connect('inventory.db')
    table_name = 'inventory_db'
    c = conn.cursor()
    success = False

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
        success = True

    except sqlite3.IntegrityError:
        print("ERROR: itemID doesn't exist!")

    # write and close DB
    conn.commit()
    conn.close()

    return success


def searchSQLRecord(inventoryItem):
    # searches the database for a matching record to the passed itemID
    # and returns a boolean T/F
    # connect to database
    conn = sqlite3.connect('inventory.db')
    table_name = 'inventory_db'
    c = conn.cursor()

    c.execute(
      '''SELECT * FROM inventory_db WHERE itemNumber=?'''
      , (inventoryItem.getItemNumber(),)
    )
    idExists = c.fetchone()

    conn.close()  # close DB connection

    if idExists:
        return True
    else:
        return False


