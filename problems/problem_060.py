# Write a function that meets these requirements.
#
# Name:       only_odds
# Parameters: a list of numbers
# Returns:    a copy of the list that only includes the
#             odd numbers from the original list
#
# Examples:
#     * input:   [1, 2, 3, 4]
#       returns: [1, 3]
#     * input:   [2, 4, 6, 8]
#       returns: []
#     * input:   [1, 3, 5, 7]
#       returns: [1, 3, 5, 7]


def only_odds(list):

    # Init var
    odds = []

    # Loop
    for i in list:
        if i % 2 == 1:
            odds.append(i)

    return odds


# Init var
list = [1, 2, 3, 4]

# Invoke and print
print(only_odds(list))
