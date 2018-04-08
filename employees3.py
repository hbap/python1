"""
Splits managers' names into first and last.

Demonstrates a CSV writer.
"""

import csv
import sys

# Check for filename
if len(sys.argv) != 3:
    sys.exit("Usage: python3 employees3.py SOURCE DEST")

# Read rows from source
rows = []
with open(sys.argv[1], "r") as file:

    # Initialize reader
    reader = csv.reader(file)

    # Read header
    header = next(reader)

    # Delete Manager from header
    del header[0]

    # Prepend ManagerLast and ManagerFirst to header
    header.insert(0, "ManagerLast")
    header.insert(1, "ManagerFirst")

    # Remember new header
    rows.append(header)

    # Iterate over rows
    for row in reader:

        # Split manager's name into first and last
        first, last = row[0].split(" ")

        # Remove Manager's full name
        del row[0]

        # Prepend manager's last name and first name to row
        row.insert(0, last)
        row.insert(1, first)

        # Remember new row
        rows.append(row)

# Write rows to destination
with open(sys.argv[2], "w") as file:
    writer = csv.writer(file)
    for row in rows:
        writer.writerow(row)
