# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(values):

    """Evaluate max"""

    # Initialize var
    max = 0

    # Loop values
    for i in values:
        if i > max:
            max = i
    return max


# Initialize var
values = [99, 98, 50, 80]

# Invoke and print
print(max_in_list(values))
