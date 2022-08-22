# Write a class that meets these requirements.
#
# Name:       Employee
#
# Required state:
#    * first name, a string
#    * last name, a string
#
# Behavior:
#    * get_fullname: should return "«first name» «last name»"
#    * get_email:    should return "«first name».«last name»@company.com"
#                    all in lowercase letters
#
# Example:
#    employee = Employee("Duska", "Ruzicka")
#
#    print(employee.get_fullname())  # prints "Duska Ruzicka"
#    print(employee.get_email())     # prints "duska.ruzicka@company.com"
#
# You may want to look at the ".lower()" method for strings to
# help with this code.
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def get_fullname(self):
        return self.first + " " + self.last

    def get_email(self):
        return self.first.lower() + self.last.lower() + "@company.com"


# Init instance
person = Employee("KARIS", "COUREY")

# Invoke method and print
print(person.get_fullname())
print(person.get_email())
