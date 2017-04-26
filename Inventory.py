# CIS320 Final Project
# Gustavo, Hugo & Seth
# SB 4/23

# Inventory class

import Validate


class Inventory:

    # set global sizes
    MIN_ITEM_NUMBER_SIZE = 1
    MAX_ITEM_NUMBER_SIZE = 9999


    # initialization def
    def __init__(self
                 , in_itemNumber = None
                 , in_itemName = None
                 , in_itemDesc = None
                 , in_stockCount = None
                 ):

        if in_itemNumber is None:
            self.__itemNumber = 0  # default case
        else:
            self.__itemNumber = in_itemNumber  # loaded constructor

        if in_itemName is None:
            self.__itemName = "_BLANK-NAME"  # default case
        else:
            self.__itemName = in_itemName  # loaded constructor

        if in_itemDesc is None:
            self.__itemDesc = "_BLANK-SHORT-DESCRIPTION"  # default case
        else:
            self.__itemDesc = in_itemDesc  # loaded constructor

        if in_stockCount is None:
            self.__stockCount = 0  # default case
        else:
            self.__stockCount = in_stockCount  # loaded constructor


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


    # default print() override
    def __str__(self):
        return str(self.__itemNumber) + "\n" \
               + self.__itemName + "\n" \
               + self.__itemDesc + "\n" \
               + str(self.__stockCount)

