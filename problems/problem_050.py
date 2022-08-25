# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]

def halve_the_list(list):

    # Init var
    list1 = []
    list2 = []

    half = len(list) / 2

    for i in list:
        if (i - 1) <= half:
            list1.append(i)
        else:
            list2.append(i)

    return list1, list2


# Init var
list = [1, 2, 3, 4, 5]

# Invoke and print
print(halve_the_list(list))
