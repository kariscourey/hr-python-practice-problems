# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"

def check_password(password):

    # Check len
    if len(password) >= 6 and len(password) <= 12:

        upper = False
        lower = False
        number = False
        character = False

        for i in password:
            if i.isupper():
                upper = True
            elif i.islower():
                lower = True
            elif i.isdigit():
                number = True
            elif i in ["$", "!", "@"]:
                character = True

        return upper and lower and number and character

    return False


# Init var
password = "kAris!12"

# Invoke and print
print(check_password(password))
