# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#

def calculate_sum(values):

    """Calculate sum"""

    # Initialize var
    sum = 0

    # Loop values
    for i in values:
        sum += i
    return sum


# Initialize var
values = []

# Invoke and print
print(calculate_sum(values))
