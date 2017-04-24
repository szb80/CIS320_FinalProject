# CIS320 Final Project
# Hugo & Seth
# SB 4/23

# Inventory class

class Inventory:

    # initialization def
    def __init__(self):
        self.__itemNumber = 000
        self.__itemName = "_BLANK NAME"
        self.__itemDesc = "_BLANK SHORT DESCRIPTION"
        self.__stockCount = 0

    def setItemNumber(self, itemNum):
        self.__itemNumber = itemNum

    def setItemName(self, itemName):
        self.__itemName = itemName

    def setItemDesc(self, itemDesc):
        self.__itemDesc = itemDesc

    
