# CIS320 Final Project
# Hugo & Seth
# SB 4/23

# Sale class

import Validate

# Initialize variables


class Sale:

    # available menu items:
    menu = ( ("Tacos", 1)
             , ("Burrito", 4)
             , ("Soda", 1.5)
             , ("Water", 1)
             )


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
                # if menu choice is within range of menu size, then set
                if 0 <= in_lineItemNum < len(Sale.menu):
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
              , "\nLine Items:  "
              , self.__lineItem
              , sep = '')
