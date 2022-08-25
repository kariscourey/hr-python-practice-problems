# Complete the reverse_dictionary function which has a
# single parameter that is a dictionary. Return a new
# dictionary that has the original dictionary's values
# for its keys, and the original dictionary's keys for
# its values.
#
# Examples:
#   * input:  {}
#     output: {}
#   * input:  {"key": "value"}
#     output: {"value", "key"}
#   * input:  {"one": 1, "two": 2, "three": 3}
#     output: {1: "one", 2: "two", 3: "three"}

def reverse_dictionary(dictionary):

    # Init var
    reverse = {}

    # Loop
    for key in dictionary:
        reverse[dictionary[key]] = key

    return reverse


# Init var
dictionary = {"one": 1, "two": 2, "three": 3}

# Invoke and print
print(reverse_dictionary(dictionary))
