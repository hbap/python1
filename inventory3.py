"""
Simulates taking inventory.

Demonstrates a dictionary.
"""

# Take inventory
inventory = {}
while True:
    item = input("Item: ")
    if not item:
        break
    if item in inventory:
        inventory[item] += 1
    else:
        inventory[item] = 1

# Report inventory
for key, value in inventory.items():
    print(f"{key}: {value}")
