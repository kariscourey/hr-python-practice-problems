# Complete the translate function which accepts two
# parameters, a list of keys and a dictionary. It returns a
# new list that contains the values of the corresponding
# keys in the dictionary. If the key does not exist, then
# the list should contain a None for that key.
#
# Examples:
#   * keys:       ["name", "age"]
#     dictionary: {"name": "Noor", "age": 29}
#     result:     ["Noor", 29]
#   * keys:       ["eye color", "age"]
#     dictionary: {"name": "Noor", "age": 29}
#     result:     [None, 29]
#   * keys:       ["age", "age", "age"]
#     dictionary: {"name": "Noor", "age": 29}
#     result:     [29, 29, 29]
#
# Remember that a dictionary has the ".get" method on it.

def translate(key_list, dictionary):

    # Init var
    result = []

    # Loop
    for i in key_list:
        if i not in dictionary:
            result.append(None)
        else:
            for j in dictionary:
                if i == j:
                    result.append(dictionary[j])

    return result


# Init var
key_list = ["eye color", "age"]
dictionary = {"name": "Noor", "age": 29}

# Invoke and print
print(translate(key_list, dictionary))
