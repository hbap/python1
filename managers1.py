"""
Assigns IDs to employees.
"""

import csv
import sys

# Check for filename
if len(sys.argv) != 2:
    sys.exit("Usage: python3 employees.py SOURCE")

# Print employees' names
with open(sys.argv[1], "r") as file:

    # Read source
    reader = csv.DictReader(file)

    # First ID
    id = 1

    # Print ID, first name, last name
    print("ID,Manager,FirstName,LastName")
    for row in reader:
        FirstName = row["FirstName"]
        LastName = row["LastName"]
        Manager = row["Manager"]
        print(f"{id},{Manager},{FirstName},{LastName}")
        id = id + 1
