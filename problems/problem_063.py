# Write a function that meets these requirements.
#
# Name:       shift_letters
# Parameters: a string containing a single word
# Returns:    a new string with all letters replaced
#             by the next letter in the alphabet
#
# If the letter "Z" or "z" appear in the string, then
# they would get replaced by "A" or "a", respectively.
#
# Examples:
#     * inputs:  "import"
#       result:  "jnqpsu"
#     * inputs:  "ABBA"
#       result:  "BCCB"
#     * inputs:  "Kala"
#       result:  "Lbmb"
#     * inputs:  "zap"
#       result:  "abq"
#
# You may want to look at the built-in Python functions
# "ord" and "chr" for this problem


def shift_letters(string):

    # Init var
    new = []

    # Loop
    for i in string:

        if i == "Z" or i == "z":
            new.append(chr(ord(i) - 25))
        else:
            new.append(chr(ord(i) + 1))

    return "".join(new)


# Init var
val = "zimport"

# Invoke and print
print(shift_letters(val))
