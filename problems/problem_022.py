# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

def gear_for_day(is_workday, is_sunny):

    """Evaluate day for gear"""

    gear = []

    if (not is_sunny) and is_workday:
        gear.append("umbrella")
    elif is_workday:
        gear.append("laptop")
    else:
        gear.append("surfboard")

    return gear


# Initialize var
is_workday = False
is_sunny = True

# Invoke and print
print(gear_for_day(is_workday, is_sunny))
