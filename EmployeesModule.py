# CIS320 Final Project
# Gustavo, Hugo & Seth
# Hugo 5/7, Seth 5/17

import Employee, EmployeeSQL, Validate, mainMenu

# GLOBAL CONSTANTS
ERROR_PROMPT = "**ERROR: That is not a valid selection."
SPACER_SIZE = 20


def displayPersonnelMenuHome(managerFlag):  # tested
    # displays the home page of the Personnel module menu
    # HM

    exitMenu = False  # set loop sentinel

    # loop through invalid input for menu display
    while not exitMenu:
        #Validate.cls()  # clear screen each run

        # print the menu
        print("EMPLOYEE MENU", "=" * SPACER_SIZE)
        print("(1)  Employees")
        print("(2)  Employees Schedule")
        print("(0)  < Go Back")

        # take user menu choice
        try:
            menuChoice = int(input())
        except ValueError:
            print(ERROR_PROMPT)
            continue  # reset loop, failure to enter correct selection

        # call sub modules
        if menuChoice == 1:  # Employees
            displayEmployeesMenu()
        elif menuChoice == 2:  # Employees Schedule
            displayEmployeeScheduleMenu()
        elif menuChoice == 0:  # return up one level
            return True  # exit function and return to calling menu
        else:  # default case
            print(ERROR_PROMPT)
    return False


def displayEmployeesMenu():  # tested
    # displays Employees
    # HM

    validMenuChoice = False  # sentinel for menu display loop
    menuChoice = -1  # initialize to -1 as sentinel

    ##Validate.cls()  # clear screen

    print("Employees ", "-" * SPACER_SIZE)

    while not validMenuChoice:
        # print the options
        print("(1)  List Employees")
        print("(2)  Add Employee")
        print("(3)  Deactivate Employee")
        print("(0)  < Go Back")

        # take user input on newline
        menuChoice = input("")

        # check if an int, else throw error and catch exception
        try:
            menuChoice = int(menuChoice)  # attempt cast to int
        except ValueError as err:
            print(ERROR_PROMPT)
            continue  # return to top of list

        # now check if int is within appropriate range
        if int(menuChoice) >= 0 or int(menuChoice) <= 3:
            validMenuChoice = True  # passes all tests and exits loop

    # input passes all tests; run search and print result
    if int(menuChoice) == 1:
        print("Here is the list of Employees:","-" * SPACER_SIZE)
        listEmployees()
        input("Press <ENTER> to continue...")

    elif int(menuChoice) == 2:
        if addEmployee():
            print("Successfully added new Employee!")
            input("Press <ENTER> to continue.")
        else:  # default case
            print("**Error adding new Employee!")
            input("Press <ENTER> to continue.")

    elif int(menuChoice) == 3:
        if deactivateEmployee():
            print("Employee has been deactivated")
            input("Press <ENTER> to continue.")
        else:  # default case
            print("No Employee was deactivated.")

    elif int(menuChoice) == 0:
        return True  # user wants to quit, exit function and return to caller

    # return to top of menu after execution
    displayEmployeesMenu()



def displayEmployees():  # tested
    # displays all Employee records in the database by calling the SQL function
    # SB
    return EmployeeSQL.displayTable()


def addEmployee():  # tested
    # adds a new employee
    # SB

    # initialize all variables to default values:
    newEmpNum = 0
    newEmpPhoneNumber = 0  # initialize to 0
    newManager = False  # default manager flag to false
    managerInt = -1  # initialize out of range
    isValid = False  # input loop sentinel

    ##Validate.cls()  # clear screen and display message
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
        if not EmployeeSQL.searchForSQLRecord(newEmpNum) \
                and Validate.validateInt(newEmpNum):
            isValid = True

    # take name to variable
    newEmpName = str(input("Enter Employee's First Name: "))

    # take last name to variable
    newEmpLastName = str(input("Enter Employee's Last Name: "))

    # take phone number and validate for number
    isValid = False  # set sentinel for input loop

    # loop until valid
    while not isValid:
        try:  # attempt to take int value
            newEmpPhoneNumber = int(input("Please Enter Employee's"
                                          "Phone Number (digits only): "))
        except ValueError:
            print("**ERROR: Must be a number!")
        if newEmpPhoneNumber:
            isValid = True  # exit loop and continue taking variables

    # take manager flag and convert to boolean
    isValid = False  # reset sentinel for input loop

    # loop until input is valid
    while not isValid:
        try:  # attempt to take int value
            managerInt = int(input("Enter '0' for Employee"
                                   "or for '1' for Manager: "))
        except ValueError:
            print("**ERROR: Not a number!")
        if managerInt in range(0,2):
            isValid = True  # is within boolean range
    # because default to False, only assign if user entered True to manager flag
    if managerInt == 1:
        newManager = True

    # all variables are now populated and validated

    # make an instance
    newEmployee = Employee.Employee(newEmpNum
                                    , newEmpName
                                    , newEmpLastName
                                    , newEmpPhoneNumber
                                    , newManager)

    # attempt write and return final status
    return EmployeeSQL.createSQLRecord(newEmployee)


def listEmployees():  # tested
    # calls the SQL function to display the table
    # SB
    return EmployeeSQL.displayTable()


def deactivateEmployee(): # tested
    # deletes an existing employee record
    # SB

    isValid = False
    employeeID = 0  # initialize to 0

    ##Validate.cls()  # clear screen and display header
    print("DELETING RECORD ", "-" * SPACER_SIZE)

    # loop menu until valid input is entered
    while not isValid:
        employeeID = input("Enter the Employee ID to delete: [0 to cancel] ")
        # check if ID is a number and loop until valid
        if not Validate.validateInt(employeeID):
            print("**ERROR: must be a number.")
            continue
        if int(employeeID) == 0:  # exit menu clause
            return False
        # check if Employee ID is not in database already and loop until valid
        if not EmployeeSQL.searchForSQLRecord(employeeID):
            print("**ERROR: ID does not exist.")
            continue

        # check if both criteria are met and exit loop
        if EmployeeSQL.searchForSQLRecord(employeeID)\
                and Validate.validateInt(employeeID):
            isValid = True

    return EmployeeSQL.deleteSQLRecord(employeeID)


def displayEmployeeScheduleMenu():  # tested
    # displays Schedule main menu
    # SB

    exitFlag = False  # set loop sentinel

    # loop through invalid input for menu display
    while not exitFlag:
        #Validate.cls()  # clear screen

        # print the menu
        print("EMPLOYEE SCHEDULING", "=" * SPACER_SIZE)
        print("(1)  Display Schedule")
        print("(2)  Modify Schedule")
        print("(0)  < Go Back")

        # take user menu choice
        try:
            menuChoice = int(input())
        except ValueError:
            print(ERROR_PROMPT)  # not an int!
            continue  # return to top of loop

        # call sub modules
        if int(menuChoice) == 1:  # Display schedule
            displayEmployeeSchedule()  # and display schedule
            input("Press <ENTER> to continue.")
        elif int(menuChoice) == 2:  # Modify Schedule
            modifyEmployeeSchedule()  # and modify schedule
            input("Press <ENTER> to continue.")
        elif int(menuChoice) == 0:  # return up one level
            exitFlag = True
            return True  # exit function and return to calling menu
        else:  # default case, out of range
            print(ERROR_PROMPT)

    displayEmployeeScheduleMenu()  # return to top of menu until exit


def displayEmployeeSchedule():  # tested
    # displays current employee schedule
    # SB
    return EmployeeSQL.displayScheduleTable()


def modifyEmployeeSchedule():  # tested
    # modifies the employee schedule
    # SB

    # initialize variables to def values:
    isValid = False  # input loop sentinel
    scheduleDay = 0
    employeeName = ""

    #Validate.cls()  # clear screen
    print("MODIFY EMPLOYEE SCHEDULE ", "-" * SPACER_SIZE)

    print("Enter the day to modify: ")
    print("\t(1) Sunday"
          , "\n\t(2) Monday"
          , "\n\t(3) Tuesday"
          , "\n\t(4) Wednesday"
          , "\n\t(5) Thursday"
          , "\n\t(6) Friday"
          , "\n\t(7) Saturday"
          )

    # input loop for day of week with validation
    while not isValid:
        try:
            scheduleDay = int(input())  # cast input as int
        except ValueError:
            print("**ERROR: Enter a number!")
            continue  # reset loop
        if scheduleDay in range(0, 8):
            isValid = True  # valid range, continue to next step
        else:
            print("**ERROR: Not a valid choice!  Too high/low.")

    # convert int to day:
    scheduleDay = convertIntToDay(scheduleDay)

    # input loop for employee name with validation
    isValid = False

    print ("Enter the employee name to schedule (case sensitive):")
    while not isValid:
        try:
            employeeName = str(input())
        except ValueError:
            print("**ERROR: Enter characters!")
        if EmployeeSQL.searchForSQLRecordName(employeeName):
            isValid = True  # record found, exit loop
        else:
            print("**ERROR: Enter a valid employee name!")

    # all validations passed, have correct date and name, now write to db

    if EmployeeSQL.updateSQLScheduleRecord(scheduleDay, employeeName):
        print("Schedule updated successfully!")
        return True
    else:  # default case
        print("**ERROR: Schedule not updated.  Record error.")
        return False


def convertIntToDay(num):  # tested
    # converts a passed int to a matching string day
    # SB
    if num == 1:
        return "Sunday"
    elif num == 2:
        return"Monday"
    elif num == 3:
        return "Tuesday"
    elif num == 4:
        return "Wednesday"
    elif num == 5:
        return "Thursday"
    elif num == 6:
        return "Friday"
    elif num == 7:
        return "Saturday"
    else:
        return "Invalid!"  # error case
