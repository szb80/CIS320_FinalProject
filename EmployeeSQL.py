# CIS320 Final Project
# Gustavo, Hugo & Seth
# SB 4/30

import Employee, sqlite3


def createSQLRecord(newEmployee):
    # creates a new SQL record for a non-existing itemNumber
    # returns boolean for successful record creation
    # + creates connection to database

    # setup database connection
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()
    success = False  # initial return condition

    try:
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


def updateSQLRecord(updateEmp):
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
        print("ERROR: itemID doesn't exist in updateSQLRecord()", err)

    # write and close DB
    conn.commit()
    conn.close()

    return success


def searchForSQLRecord(empNum):
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


def createEmployeeFromSQLRecord(empNum):
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
            '''SELECT * FROM inventory_db WHERE itemNumber=?'''
            , (empNum,))
        idExists = c.fetchone()

        # close connection without commit
        conn.close()

        # build Inventory instance to return with 4 columns
        return Employee.Employee(idExists[0]
                                   , idExists[1]
                                   , idExists[2]
                                   , idExists[3]
                                   )

    else:
        return None


def deleteSQLRecord(empNum):
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
