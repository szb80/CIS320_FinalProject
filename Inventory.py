# CIS320 Final Project
# Hugo & Seth
# SB 4/23

# Inventory class

import Validate, sqlite3


class Inventory:

    # initialization def
    def __init__(self):
        self.__itemNumber = 000
        self.__itemName = "_BLANK NAME"
        self.__itemDesc = "_BLANK SHORT DESCRIPTION"
        self.__stockCount = 0


    def setItemNumber(self, itemNum):
        if Validate.validateInt(itemNum):
            self.__itemNumber = itemNum
            return True
        return False


    def setItemName(self, itemName):
        if Validate.validateString(itemName):
            self.__itemName = itemName
            return True
        return False


    def setItemDesc(self, itemDesc):
        if Validate.validateString(itemDesc):
            self.__itemDesc = itemDesc
            return True
        return False


    def setStockCount(self, updatedCount):
        if Validate.validateInt(updatedCount):
            self.__stockCount = updatedCount
            return True
        return False


    def getItemNumber(self):
        return self.__itemNumber


    def getItemName(self):
        return self.__itemName


    def getItemDesc(self):
        return self.__itemDesc


    def getStockCount(self):
        return self.__stockCount


    def displayInventory(self):
        print(self.__itemNumber
              , self.__itemName
              , self.__itemDesc
              , self.__stockCount)

    def displayInventory(self, itemNum):  ######################################
        self.searchInventory(itemNum)  # search for item number and
        self.displayInventory(itemNum)  # display for returned inventory item


    def searchInventory(self, searchStr):
        # SEARCHES INVENTORY DB FOR NAME MATCHING searchStr  ###################
        # returns matching inventory instance ##################################
        return True


    def searchInventory(self, itemNum):
        # SEARCHES INVENTORY DB FOR ITEM NUM MATCHING ARGUMENT #################
        # returns matching inventory instance ##################################
        return True

