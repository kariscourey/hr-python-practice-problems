# Write a function that meets these requirements.
#
# Name:       sum_fraction_sequence
# Parameters: a number
# Returns:    the sum of the fractions of the
#             form 1/2+2/3+3/4+...+number/number+1
#
# Examples:
#     * input:   1
#       returns: 1/2
#     * input:   2
#       returns: 1/2 + 2/3
#     * input:   3
#       returns: 1/2 + 2/3 + 3/4


def sum_fraction_sequence(num):

    # Init var
    sum = ""

    # Loop
    for i in range(1, num):
        sum += str(i) + "/" + str((i + 1))

        if i != (num - 1):
            sum += " + "

    return sum


# Init var
num = 5

# Invoke and print
print(sum_fraction_sequence(num))
