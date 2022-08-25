# Write a function that meets these requirements.
#
# Name:       specific_random
# Parameters: none
# Returns:    a random number between 10 and 500, inclusive,
#             that is divisible by 5 and 7
#
# Examples:
#     * returns: 35
#     * returns: 105
#     * returns: 70
#
# Guidance:
#   * Generate all the numbers that are divisible by 5
#     and 7 into a list
#   * Use random.choice to select one

from random import randint


def specific_random():

    # Init var
    num = 0

    # Loop
    while num == 0:

        temp = randint(10, 500)

        if temp % 5 == 0 and temp % 7 == 0:
            num += temp

    return num


# Invoke and print
print(specific_random())
