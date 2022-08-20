# Complete the can_make_pasta function to
# * Return true if the ingredients list contains
#   "flour", "eggs", and "oil"
# * Otherwise, return false
#
# The ingredients list will always contain three items.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def can_make_pasta(ingredients):

    """Evaluate ingredients for pastability"""

    # Initialize var
    pasta_ingredients = ['flour', 'eggs', 'oil']

    # Compare
    for i in pasta_ingredients:
        if i not in ingredients:
            return False
    return True


# Initialize var
ingredients = ['flour', 'oil', 'water', 'sugar', 'eggs']

# Invoke and print
print(can_make_pasta(ingredients))
