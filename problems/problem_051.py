# Write a function that meets these requirements.
#
# Name:       safe_divide
# Parameters: two values, a numerator and a denominator
# Returns:    if the denominator is zero, then returns math.inf.
#             otherwise, returns numerator / denominator
#
# Don't for get to import math!

import math


def safe_divide(num, den):

    if den != 0:
        return num/den
    return math.inf


# Init var
num1, num2 = 2, 1

# Invoke and print
print(safe_divide(num1, num2))
