# Complete the minimum_value function so that returns the
# minimum of two values.
#
# If the values are the same, return either.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def minimum_value(value1, value2):

    """Evaluate 2 values for min"""

    if value1 <= value2:
        return value1
    if value1 > value2:
        return value2


# Initialize var
value1 = 10
value2 = 2

# Invoke and print
print(minimum_value(value1, value2))
