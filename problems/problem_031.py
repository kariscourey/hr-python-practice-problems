# Complete the sum_of_squares function which accepts
# a list of numerical values and returns the sum of
# each item squared
#
# If the list of values is empty, the function should
# return None
#
# Examples:
#   * [] returns None
#   * [1, 2, 3] returns 1*1+2*2+3*3=14
#   * [-1, 0, 1] returns (-1)*(-1)+0*0+1*1=2
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def sum_of_squares(values):

    # Init var
    sum = 0

    # Loop
    for i in values:
        square = i * i
        sum += square
    return sum


# Initialize var
values = [1, 2, 3]

# Invoke and print
print(sum_of_squares(values))
