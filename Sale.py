# CIS320 Final Project
# Hugo & Seth
# SB 4/23

# Sale class

import Validate, datetime

# Initialize variables


class Sale:

    # initialization def
    def __init__(self):
        self.__saleNumber = datetime.datetime.now(datetime.timezone.utc)
        self.__lineItem = [ ]


    def setSaleLineItems(self, lineItems):
        return self.__lineItem == lineItems


    def __str__(self):
        print("Sale #", self.__saleNumber
              , "\nLine Items:  "
              , self.__lineItem
              , sep = '')
