"""
Simulates taking inventory.

Demonstrates a sorted list (potentially with duplicates).
"""

# Take inventory
inventory = []
while True:
    item = input("Item: ")
    if not item:
        break
    inventory.append(item)

# Report inventory
for item in sorted(inventory):
    print(item)
