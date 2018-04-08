"""
Prints employees' names.

Demonstrates a DictReader.
"""

import csv
import sys

# Check for filename
if len(sys.argv) != 2:
    sys.exit("Usage: python3 employees2.py FILE")
filename = sys.argv[1]

# Print employees' names
with open(filename, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["FirstName"], row["LastName"])
