# CIS320 Final Project
# Hugo & Seth
# SB 4/23

# Sale class defines a sale line item object for writing to the database
# Each sale may have one or more line items written to the database

import Validate

class Sale:
    # initialization def
    def __init__(self
                 , in_saleNumber = None
                 , in_lineItemNum = None
                 , in_lineItemQty = None
                 ):
        if in_saleNumber is None:
            self.__saleNumber = 0  # default case
        else:  # set to passed argument
            self.__saleNumber = in_saleNumber

        if in_lineItemNum is None:
            self.__lineItemNum = 0  # default case
        else:  # set to passed argument
            try:  # check for passed string instead of int
                # if menu choice is within range, then set
                if in_lineItemNum > 0:
                    self.__lineItemNum = in_lineItemNum
            except ValueError:
                self.__lineItemNum = 0  # set to default upon failure

        if in_lineItemQty is None:
            self.__lineItemQty = 0  # default case
        else:  # set to passed argument
            self.__lineItemQty = in_lineItemQty


    # setters
    def setSaleLineItemNum(self, lineItemNum):
        if Validate.validateInt(lineItemNum):  # validate first
            self.__lineItem == lineItemNum  # then set value
            return True
        return False  # otherwise return false


    def setSaleLineItemQty(self, lineItemQty):
        if Validate.validateInt(lineItemQty):  # validate first
            self.__lineItemQty = lineItemQty  # then set value
            return True
        return False  # otherwise return false


    # getters
    def getSaleNumber(self):
        return self.__saleNumber  # return value


    def getSaleLineItemNum(self):
        return self.__lineItemNum  # return value


    def getSaleLineItemQty(self):
        return self.__lineItemQty  # return value


    # default print override
    def __str__(self):
        print("Sale #", self.__saleNumber
              , "\t"
              , self.__lineItemNum
              , "\t"
              , self.__lineItemQty
              , sep = '')
