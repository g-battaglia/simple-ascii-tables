# Simple Ascii Tables

A simple, minimal and *dependency-free* python package for generating ascii tables.

It's a simplified fork of terminaltables.

## Why another fork?

Terminal Tables was a super cool project. It's no more maintained sadly.
There are some forks but they're too much complex for a basic usage.
There is also Rich library which is awesome but it's bloated for a simple ascii table with no dependencies.


## Installation

```bash
pip install simple-ascii-tables
```

## Usage

```python
from simple_ascii_tables import AsciiTable

table_data = [
    ["Name", "Age", "Country"],
    ["Alice", 24, "Canada"],
    ["Bob", 19, "USA"],
    ["Charlie", 30, "Australia"],
]

table = AsciiTable(table_data)
print(table.table)
```

Output:

```plaintext
+User Information-----------+
| Name    | Age | Country   |
+---------+-----+-----------+
| Alice   | 24  | Canada    |
| Bob     | 19  | USA       |
| Charlie | 30  | Australia |
+---------+-----+-----------+
```
