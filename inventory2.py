"""
Simulates taking inventory.

Demonstrates a set (without duplicates).
"""

# Take inventory
inventory = set()
while True:
    item = input("Item: ")
    if not item:
        break
    inventory.add(item)

# Report inventory
for item in sorted(inventory):
    print(item)
