#!/usr/bin/env python
from simple_ascii_tables import AsciiTable

table_data = [
    ["Name", "Age", "Country"],
    ["Alice", 24, "Canada"],
    ["Bob", 19, "USA"],
    ["Charlie", 30, "Australia"],
]

table = AsciiTable(table_data)
table.title = "User Information"
print(table.table)
