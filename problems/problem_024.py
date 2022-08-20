# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

def calculate_average(values):

    """Calculate average"""

    # Initialize var
    sum = 0
    count = 0

    if values:
        # Loop values
        for i in values:
            sum += i
            count += 1
        return sum / count


# Initialize var
values = []

# Invoke and print
print(calculate_average(values))
