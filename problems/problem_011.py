# Complete the is_divisible_by_5 function to return the
# word "buzz" if the value in the number parameter is
# divisible by 5. Otherwise, just return the number.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def is_divisible_by_5(number):

    """Evaluate number for divisible by 5"""

    if number % 5 == 0:
        return "buzz"
    else:
        return number


# Initialize var
num = 12

# Invoke and print
print(is_divisible_by_5(num))
