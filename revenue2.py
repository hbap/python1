"""
Calculates average daily revenue.

Demonstrates a package.
"""

from calendar import day_abbr

# Sum daily revenues
revenue = 0.0
for day in day_abbr:
    revenue += float(input(f"{day}: $"))

# Calculate average
average = revenue / len(day_abbr)
print(f"Ave: ${average:.2f}")
