# test file for debugging

import Inventory, InventoryModule, InventorySQL, Validate

flour = Inventory.Inventory()
loaded = Inventory.Inventory(37, "37 Loaded", "37 loaded function call", 97)

#InventorySQL.createSQLRecord(loaded)

#InventorySQL.createInventoryFromSQLRecord(37)

#print(InventorySQL.searchForSQLRecord(37))

#print(InventorySQL.deleteSQLRecord(37))

#InventoryModule.displayCheckInventoryMenu()

#InventoryModule.displayModifyInventoryMenu()

#InventoryModule.displayInventoryMenuHome()

InventorySQL.displayTable()
