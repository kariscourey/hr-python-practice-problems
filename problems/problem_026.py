# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average

def calculate_grade(values):

    """Calculate grade"""

    # Initialize var
    sum = 0
    count = 0

    # Loop values
    for i in values:
        sum += i
        count += 1

    avg = sum / count

    # Evaluate avg
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


# Initialize var
values = [99, 98, 100, 80]

# Invoke and print
print(calculate_grade(values))
