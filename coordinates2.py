"""
Calculates the distance between two points.

Demonstrates indexing into tuples.
"""

from math import sqrt

# Two points
a = (0, 0)
b = (50, 50)

# Calculate distance
distance = sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
print(distance)
