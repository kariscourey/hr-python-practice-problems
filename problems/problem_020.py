# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.

def has_quorum(attendees_list, members_list):

    """Evaluate attendees for majority"""

    return (len(attendees_list) >= 0.50 * len(members_list))


# Initialize var
attendees_list = ['foo']
members_list = ['foo', 'bar', 'baz']

# Invoke and print
print(has_quorum(attendees_list, members_list))
