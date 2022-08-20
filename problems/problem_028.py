# Complete the remove_duplicate_letters that takes a string
# parameter "s" and returns a string with all of the
# duplicates removed.
#
# Examples:
#   * For "abc", the result is "abc"
#   * For "abcabc", the result is "abc"
#   * For "abccba", the result is "abc"
#   * For "abccbad", the result is "abcd"
#
# If the list is empty, then return the empty string.

def remove_duplicate_letters(s):

    """Remove duplicate letters from string"""

    # Init var
    letters = []

    # Loop s
    for i in s:
        if i not in letters:
            letters.append(i)

    # Join elements of iterable
    string = "".join(letters)
    return string


# Init var
s = "ssstriiiiiingg"

# Invoke and print
print(remove_duplicate_letters(s))
