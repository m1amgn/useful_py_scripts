# Automate Excel Files
# pip install xlwings

import xlwings as ex

wb = ex.Book("test.xlsx")
ws = wb.sheets[0]

# Read Data Cell 
print(ws.range("A1").value)

# Read Data Row
print(ws.range("A1:A3").value)

# Read Data Column
print(ws.range("A1:C3").value)

# Write Data to Cell
ws.range("A1").value = "Hello World"

# Write Data to Row
ws.range("A1:A3").value = ["Hello", "World", "!"]

# Write Data to Column
ws.range("A1:C3").value = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Save 
wb.save()
