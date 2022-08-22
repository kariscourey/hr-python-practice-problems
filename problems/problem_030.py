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

# def find_second_largest(values):

# # Init var
# s_values = sorted(values)

# # Return
# return s_values[-2]


def find_second_largest(values):

    # Init
    max = values[0]
    second = values[0]

    # Loop for max
    for i in values:
        if i > max:
            second = max
            max = i
        if i < max and i > second:
            second = i

    # think through:
    # 80, 100, 90
    # second = 0, max = 80 //
    # second = 80, max = 100 //
    # // second = 90, max = 100

    # # Loop for max -- doesn't work for duplicates
    # for i in values:
    #     if i > second:
    #         second = i
    #         if second > max:
    #             max_old = max
    #             max = second
    #             second = max_old

    # # Loop for max -- works for duplicates, but two loops
    # for i in values:
    #     if i > max:
    #         max = i

    # # Loop for second
    # for i in values:
    #     if i > second and i < max:
    #         second = i

    return max, second


# Initialize var
values = [70, 80, 90, 102, 98, 102, 101, 110, 110, 99.5]

# Invoke and print
print(find_second_largest(values))
