#!/usr/bin/env python
"""Simple example usage of simple_ascii_tables without any other dependencies.

Just prints sample text and exits.
"""

from __future__ import print_function

from simple_ascii_tables import AsciiTable

TABLE_DATA = (
    ('Platform', 'Years', 'Notes'),
    ('Mk5', '2007-2009', 'The Golf Mk5 Variant was\nintroduced in 2007.'),
    ('MKVI', '2009-2013', 'Might actually be Mk5.'),
    ('NK33',  '20013-2030', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam nec odio vestibulum, vehicula elit nec, fermentum nunc.'),
)


def main():
    """Main function."""
    title = 'Jetta SportWagen'

    # AsciiTable.
    table_instance = AsciiTable(TABLE_DATA, title, max_column_width=40)
    table_instance.justify_columns[2] = 'right'

    print(table_instance.table)


if __name__ == '__main__':
    main()
