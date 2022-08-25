# Complete the pairwise_add function which accepts two lists
# of the same size. It creates a new list and populates it
# with the sum of corresponding entries in the two lists.
#
# Examples:
#   * list1:  [1, 2, 3, 4]
#     list2:  [4, 5, 6, 7]
#     result: [5, 7, 9, 11]
#   * list1:  [100, 200, 300]
#     list2:  [ 10,   1, 180]
#     result: [110, 201, 480]
#
# Look up the zip function to help you with this problem.

def pairwise_add(list1, list2):

    # Init var
    zipped = list(zip(list1, list2))

    # Loop
    for i in zipped:
        sum = 0

        for j in i:
            sum += j

            # TODO
            # try:
            list1[list1.index(j)] = sum
            # except ValueError:
                # pass

    return list1


# Init var
list1 = [100, 200, 300]
list2 = [10, 1, 180]

# Invoke and print
print(pairwise_add(list1, list2))
