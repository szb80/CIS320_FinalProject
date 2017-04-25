# CIS320 Final Project
# Hugo & Seth
# SB 4/23

# Inventory class

import Validate

class Inventory:

    # set global sizes
    MIN_ITEM_NUMBER_SIZE = 1
    MAX_ITEM_NUMBER_SIZE = 9999


    # initialization def
    def __init__(self):
        self.__itemNumber = 0
        self.__itemName = "_BLANK NAME"
        self.__itemDesc = "_BLANK SHORT DESCRIPTION"
        self.__stockCount = 0


    # setters
    def setItemNumber(self, itemNum):
        if Validate.validateInt(itemNum):
            if itemNum >= Inventory.MIN_ITEM_NUMBER_SIZE \
                and itemNum <= Inventory.MAX_ITEM_NUMBER_SIZE:
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


    # getters
    def getItemNumber(self):
        return self.__itemNumber


    def getItemName(self):
        return self.__itemName


    def getItemDesc(self):
        return self.__itemDesc


    def getStockCount(self):
        return self.__stockCount


    def getMIN_ITEM_NUMBER_SIZE(self):
        return self.MIN_ITEM_NUMBER_SIZE


    def getMAX_ITEM_NUMBER_SIZE(self):
        return self.MAX_ITEM_NUMBER_SIZE


    # default print() override
    def __str__(self):
        print(self.__itemNumber
              , self.__itemName
              , self.__itemDesc
              , self.__stockCount)






    # NOT USED IN SPEC #########################################################
    def displayInventory(self, itemNum):  ######################################
        self.searchInventory(itemNum)  # search for item number and
        self.displayInventory(itemNum)  # display for returned inventory item
