"""
Compares two integers.

Demonstrates conditions and relational operators.
"""

# Prompt user for revenue
revenue = int(input("Revenue: "))

# Prompt user for costs
costs = int(input("Costs: "))

# Compare revenue and costs
if revenue > costs:
    print("Profitable")
elif revenue < costs:
    print("Unprofitable")
else:
    print("Broke even")
