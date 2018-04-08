"""
Calculates average daily revenue.

Demonstrates a for loop and list.
"""

# Sum daily revenues
revenue = 0.0
for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
    revenue += float(input(f"{day}: $"))

# Calculate average
average = revenue / 7
print(f"Ave: ${average:.2f}")
