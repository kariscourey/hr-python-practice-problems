# Complete the can_skydive function so that determines if
# someone can go skydiving based on these criteria
#
# * The person must be greater than or equal to 18 years old, or
# * The person must have a signed consent form

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def can_skydive(age, has_consent_form):

    """Evaluate age, has_consent_form for ability to skydive"""

    # Return bool
    return age >= 18 or has_consent_form


# Initialize var
age = 12
consent = True

# Invoke and print
print(can_skydive(age, consent))
