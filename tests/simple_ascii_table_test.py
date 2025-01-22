from simple_ascii_tables import AsciiTable

def test_table_output():
    table_data = [
        ["Name", "Age", "Country"],
        ["Alice", 24, "Canada"],
        ["Bob", 19, "USA"],
        ["Charlie", 30, "Australia"],
    ]

    table = AsciiTable(table_data)
    expected_output = (
        "+---------+-----+-----------+\n"
        "| Name    | Age | Country   |\n"
        "+---------+-----+-----------+\n"
        "| Alice   | 24  | Canada    |\n"
        "| Bob     | 19  | USA       |\n"
        "| Charlie | 30  | Australia |\n"
        "+---------+-----+-----------+"
    )

    assert table.table == expected_output

