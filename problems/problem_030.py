# Complete the find_second_largest function which accepts
# a list of numerical values and returns the second largest
# in the list
#
# If the list of values is empty, the function should
# return None
#
# If the list of values has only one value, the function
# should return None
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def find_second_largest(values):

    # Init var
    s_values = sorted(values)

    # Return
    return s_values[-2]


# Initialize var
values = [99, 98, 50, 80, 100, 99.5]

# Invoke and print
print(find_second_largest(values))
