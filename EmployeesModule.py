# GLOBAL CONSTANTS
ERROR_PROMPT = "**ERROR: That is not a valid selection, try again."
SPACER_SIZE = 20


# displays the home page of the Personnel module menu
def displayPersonnelMenuHome():  # ++++++++++++++++++++++++++++++++++++++++++++
    validMenuChoice = False

    # loop through invalid input for menu display
    while not validMenuChoice:
        # print the menu
        print("INVENTORY MENU", "=" * SPACER_SIZE)
        print("1) Employees")
        print("2) Employees Schedule")
        print("0) Return")

        # take user menu choice
        try:
            menuChoice = int(input())
        except ValueError:
            print(ERROR_PROMPT)
            continue

        # call sub modules
        if menuChoice == 1:  # Employees
            validMenuChoice = True
            displayEmployeesMenu()
        elif menuChoice == 2:  # Employees Schedule
            validMenuChoice = True
            displayEmployeeSchedule()
        elif menuChoice == 0:  # return up one level
            return True  # exit function and return to calling menu
        else:  # default case
            print(ERROR_PROMPT)



def displayEmployeesMenu():  #+++++++++++++++++++++++++++++++++++++++++++
    # displays Employees
    validMenuChoice = False  # sentinel for menu display loop
    menuChoice = -1  # initialize to -1 as sentinel

    #Validate.cls()  # clear screen

    print("Employees ", "-" * SPACER_SIZE)

    while not validMenuChoice:
        # print the options
        print("(1)  List Employees")
        print("(2)  Add Employee")
        print("(3)  Deactivate Employee")
        print("(0)  Return")

        # take user input on newline
        menuChoice = input("")

        # check if an int, else throw error and catch exception
        try:
            menuChoice = int(menuChoice)  # attempt cast to int
        except ValueError as err:
            print(ERROR_PROMPT, " at displayEmployees() ", err)

        # now check if int is within appropriate range
        if int(menuChoice) >= 0 or int(menuChoice) <= 3:
            validMenuChoice = True  # passes all tests and exits loop

    # input passes all tests; run search and print result
    if int(menuChoice) == 1:
        if listEmployees():
            print("Here is the list of Employees:","-" * SPACER_SIZE)
        else:  # default case
            print("Could not find Employees!")

    elif int(menuChoice) == 2:
        if addEmployees():
            print("Successfully added new Employee")
        else:  # default case
            print("Error adding new Employee")

    elif int(menuChoice) == 3:
        if deactivateEmployee():
            print("employee has been deactivated")
        else:  # default case
            print("No Employee was deactivated.")


    elif int(menuChoice) == 0:
        return True  # user wants to quit, exit function and return to caller

    # error case, should not hit during normal execution
    else:
        displayEmployeesMenu()

    # return to Inventory home menu
    displayInventoryMenuHome()


def displayEmployees():  # ++++++++++++++++++++++++++++++++++++++++++++++++++
    # displays all the Employee records in the database
    return EmployeeSQL.displayTable()


def addEmployee():  # +++++++++++++++++++++++++++++++++++++++++++++++++++++
    # adds a new inventory item
    isValid = False

    #Validate.cls()  # clear screen

    print("ADDING NEW EMPLOYEE ", "-" * SPACER_SIZE)

    while not isValid:
        newEmpNum = input("Enter a New Employee Number: ")
        # check if ID is a number and loop until valid
        if not Validate.validateInt(newEmpNum):
            print("**ERROR: must be a number.")
        # check if ID is in database already and loop until valid
        if EmployeeSQL.searchForSQLRecord(newEmpNum):
            print("**ERROR: ID already exists.")

        # check if both criteria are met and exit loop
        if not EmployeeSQL.searchForSQLRecord(newItemNum) \
                and Validate.validateInt(newItemNum):
            isValid = True

    newEmpName = str(input("Enter Employees First Name: "))  # take name
    newEmpLastName = str(input("Enter Employees Las Name: "))  # take last name
    newEmpPhoneNumber = int(input("Please Enter Employees Phone Number in The Format XXX-XXX-XXXX"))  # take description
    newManager = input("Enter the stock count: ")  # take stock count
    while not Validate.getMaanager(newManager): # validate is manager

    # all variables now populated and validated

    # make an object
    newEmployee = Employee.Employee(newEmpNum, newEmpName, newEmpLastName, newEmpPhoneNumber, newManager)
    # attempt write and return status
    return EmployeeSQL.createSQLRecord(newEmployee)



def deactivateEmployee(): # ++++++++++++++++++++++++++++++++++++++++++++++++++
    # deletes an existing inventory record
    isValid = False

    #Validate.cls()

    print("DELETING RECORD ", "-" * SPACER_SIZE)

    # loop menu until valid input is entered
    while not isValid:
        employeeID = input("Enter the Employee ID to delete: [0 to cancel] ")
        # check if ID is a number and loop until valid
        if not Validate.validateInt(employeeID):
            print("**ERROR: must be a number.")
            continue
        if int(itemID) == 0:
            return False
        # check if Employee ID is not in database already and loop until valid
        if not EmployeeSQL.searchForSQLRecord(employeeID):
            print("**ERROR: ID does not exist.")

        # check if both criteria are met and exit loop
        if EmployeeSQL.searchForSQLRecord(employeeID) and Validate.validateInt(employeeID):
            isValid = True

    return EmployeeSQL.deleteSQLRecord(itemID)
