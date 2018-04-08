"""
Prints employees' names.

Demonstrates a command-line argument, exiting, and a CSV reader.
"""

import csv
import sys

# Check for filename
if len(sys.argv) != 2:
    sys.exit("Usage: python3 employees1.py FILE")
filename = sys.argv[1]

# Print employees' names
with open(filename, "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row[2], row[1])
