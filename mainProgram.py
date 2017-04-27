# CIS320 Final Project
# Hugo & Seth
# SB 4/20

#import mainMenu, validate, sqlite3

def getEmployeeNumber():
    while True:
        try:
            userLogin = int(input("Please enter your Employee Number: "))
        except ValueError:
            print("Sorry Invalid Input.")
            return getEmployeeNumber()

        if userLogin < 1:
            print("Sorry Invalid Input.")
            return getEmployeeNumber()

        elif userLogin > 100:
            print("Sorry Invalid Input.")
            return getEmployeeNumber()
        else:
            break
    return userLogin

getEmployeeNumber()







#Ask for User Employee ID#
#def inputUserLogin():
   # userLogin = int(input("Please Enter your Employee Number: "))
    #return userLogin






#managerFlag = setManagerFlag( userLogin() )

#mainMenu(managerFlag)

