# CIS320 Final Project
# Gustavo, Hugo & Seth
# SB 5/6

import Sale, sqlite3


def displayRecord(empID): # --------------------------------------------------
    # displays a single record from the database
    # returns boolean for successful
    # + creates connection to database

    # search for record to delete
    try:
        # connect to database
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()

        # select record
        c.execute(
            '''SELECT * FROM employee_db WHERE empNumber=?'''
            , (empID,)
        )
        idExists = c.fetchone()  # load record into variable

        if idExists:
            displayEmployee = createEmployeeFromSQLRecord(empID)

        # print record formatted
        print(displayEmployee)
        #print('Employee Number:\t{0}\nEmployee Name:\t\t{1} {2}\nEmployee Phone:\t\t{3}\nIs A Manager?:\t\t{4}\n'.format(idExists[0], idExists[1], idExists[2], idExists[3], idExists[4]))

        # close the file and return successful
        conn.close()
        return True

    # catch any errors and return false
    except sqlite3.IntegrityError as err:
        print("**ERROR: at displayRecord()", err)
    return False


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


def createSQLRecord(newSale): # ------------------------------------------
    # creates a new SQL record for a non-existing itemNumber
    # returns boolean for successful record creation
    # + creates connection to database

    success = False  # initial return condition

    if searchForSQLRecord(newEmployee.getEmpNumber()):
        return success  # record already exists, abort

    try:
        # setup database connection
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()

        # try to execute insert record command on c
        c.execute("INSERT INTO employee_db VALUES(?, ?, ?, ?, ?)"
                  , (newEmployee.getEmpNumber()
                     , newEmployee.getEmpNameFirst()
                     , newEmployee.getEmpNameLast()
                     , newEmployee.getEmpPhone()
                     , newEmployee.getManager()
                     )
                  )
        success = True  # successful creation of record

    except sqlite3.IntegrityError as err:
        print("ERROR: itemID already exists!  createSQLRecord()", err)

    # write and close db
    conn.commit()
    conn.close()

    return success


def updateSQLRecord(updateEmp): # ---------------------------------------------
    # updates an existing SQL record
    # returns boolean for record updated successfully
    # + creates connection to database

    # setup database connection
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()
    success = False  # initial return condition

    try:
        # try to execute update matching record command on c
        c.execute(
            "UPDATE employee_db SET empNameFirst=?, empNameLast=?, empPhone=?, manager=? WHERE empNumber=?"
            , (updateEmp.getEmpNameFirst()
               , updateEmp.getEmpNameLast()
               , updateEmp.getEmpPhone()
               , updateEmp.getManager()
               , updateEmp.getEmpNumber()
               )
        )
        success = True  # successful update record

    except sqlite3.IntegrityError as err:
        print("ERROR: empNumber doesn't exist in updateSQLRecord()", err)

    # write and close DB
    conn.commit()
    conn.close()

    return success


def searchForSQLRecord(empNum): # --------------------------------------------
    # searches the database for a matching record to the passed itemID
    # returns a boolean for record is found
    # + creates connection to database

    # connect to database
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()

    # select record
    c.execute(
      '''SELECT * FROM employee_db WHERE empNumber=?'''
      , (empNum,)
    )
    idExists = c.fetchone()

    conn.close()  # close DB connection without commit

    if idExists:  # record was found in DB
        return True
    else:
        return False


def createEmployeeFromSQLRecord(empNum): # ----------------------------------
    # takes a passed itemID and creates an Inventory instance
    # with the data returned from the record
    # returns Inventory instance for matching itemID
    # + creates connection to database

    if searchForSQLRecord(empNum):  # record exists
        # connect to database
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()

        # select row from
        c.execute(
            '''SELECT * FROM employee_db WHERE empNumber=?'''
            , (empNum,))
        idExists = c.fetchone()

        # close connection without commit
        conn.close()

        # build Inventory instance to return with 4 columns
        return Employee.Employee(idExists[0]
                                   , idExists[1]
                                   , idExists[2]
                                   , idExists[3]
                                   , idExists[4]
                                   )

    else:
        return None


def deleteSQLRecord(empNum): # -----------------------------------------------
    # drops a record from the database
    # returns boolean for successful
    # + creates connection to database

    # search for record to delete
    if searchForSQLRecord(empNum):
        try:
            # connect to database
            conn = sqlite3.connect('employee.db')
            c = conn.cursor()
            conn.execute('''DELETE from employee_db where empNumber=?'''
                         , (empNum,))

            # commit and execute
            conn.commit()
            conn.close()

            return True

        except sqlite3.IntegrityError as err:
            print("**ERROR: at deleteSQLRecord()", err)

    return False