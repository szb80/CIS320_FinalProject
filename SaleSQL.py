# CIS320 Final Project
# Gustavo, Hugo & Seth
# SB 5/6

import sqlite3


def displaySale(saleNum): # --------------------------------------------------------
    # displays all records for a single sale number from the database
    # returns boolean for successful
    # + creates connection to database

    # search for record to delete
    try:
        # connect to database
        conn = sqlite3.connect('sales.db')
        c = conn.cursor()

        # select all rows
        c.execute(
            '''SELECT * FROM sales_db WHERE saleNumber=?'''
            , (saleNum,)
        )
        result = c.fetchall()

        for row in result:
            print('MenuItemID:\t{1}\nQuantity:\t\t{2}'.format(row[1], row[2]))

        # close the file
        conn.close()

        return True

    # catch any errors in the file
    except sqlite3 as err:
        print("**ERROR: at displaySale()", err)

    return False


def returnSaleQuantity(saleNum, menuID): # --------------------------------------------------------
    # displays all records for a single sale number from the database
    # returns boolean for successful
    # + creates connection to database

    # search for record to delete
    try:
        # connect to database
        conn = sqlite3.connect('sales.db')
        c = conn.cursor()

        # select all rows
        c.execute(
            '''SELECT * FROM sales_db WHERE saleNumber=? AND lineItemNum=?'''
            , (saleNum, menuID,)
        )
        result = c.fetchall()

        qty = 0  # initialize to 0

        for row in result:
            qty += row[2]

        # close the file
        conn.close()

        return qty

    # catch any errors in the file and return empty
    except sqlite3 as err:
        print("**ERROR: at displaySale()", err)

    return None


def createSQLRecord(newSale): # ------------------------------------------
    # creates a new SQL record for a non-existing saleNumber
    # returns boolean for successful record creation
    # + creates connection to database

    success = False  # initial return condition

    try:
        # setup database connection
        conn = sqlite3.connect('sales.db')
        c = conn.cursor()

        # try to execute insert record command on c
        c.execute("INSERT INTO sales_db VALUES(?, ?, ?)"
                  , (newSale.getSaleNumber()
                     , newSale.getSaleLineItemNum()
                     , newSale.getSaleLineItemQty()
                     )
                  )
        success = True  # successful creation of record

    except sqlite3.IntegrityError as err:
        print("ERROR: itemID already exists!  createSQLRecord()", err)

    # write and close db
    conn.commit()
    conn.close()

    return success


def updateSQLRecordQty(saleNum, menuItem, newQty): # tested
    # updates an existing SQL record
    # returns boolean for record updated successfully
    # + creates connection to database

    # setup database connection
    conn = sqlite3.connect('sales.db')
    c = conn.cursor()
    success = False  # initial return condition

    try:
        # connect to database
        conn = sqlite3.connect('sales.db')
        c = conn.cursor()

        # attempt search on database for passed arguments
        c.execute(
            '''SELECT * FROM sales_db WHERE saleNumber=? AND lineItemNum=?'''
            , (saleNum, menuItem,)
        )

        # attempt save first result to variable
        # there should only be one result
        idExists = c.fetchone()

        # if successful
        if idExists:
            # delete the current entry
            conn.execute(
                '''DELETE from sales_db where saleNumber=? AND lineItemNum=?'''
                , (saleNum, menuItem,)
            )
            # recreate the new line item with the updated qty value
            c.execute("INSERT INTO sales_db VALUES(?, ?, ?)"
                      , (saleNum, menuItem, newQty,)
                      )

            success = True  # exit result

        # commit changes to database
        conn.commit()
        conn.close()

    except sqlite3.IntegrityError as err:
        print("**ERROR: at deleteSQLRecord()", err)

    return success


def searchForSQLRecord(saleNum): # --------------------------------------------
    # searches the database for a matching record to the passed itemID
    # returns a boolean for record is found
    # + creates connection to database

    # connect to database
    conn = sqlite3.connect('sales.db')
    c = conn.cursor()

    # select record
    c.execute(
      '''SELECT * FROM sales_db WHERE saleNumber=?'''
      , (saleNum,)
    )
    idExists = c.fetchall()

    conn.close()  # close DB connection without commit

    if idExists:  # record was found in DB
        return True
    else:
        return False


def deleteSQLRecord(saleNum): # -----------------------------------------------
    # drops a record from the database
    # returns boolean for successful
    # + creates connection to database

    # search for record to delete
    if searchForSQLRecord(saleNum):
        try:
            # connect to database
            conn = sqlite3.connect('sales.db')
            c = conn.cursor()
            conn.execute('''DELETE from sales_db where saleNumber=?'''
                         , (saleNum,))

            # commit and execute
            conn.commit()
            conn.close()

            return True

        except sqlite3.IntegrityError as err:
            print("**ERROR: at deleteSQLRecord()", err)

    return False

