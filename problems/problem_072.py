# Write a class that meets these requirements.
#
# Name:       Person
#
# Required state:
#    * name, a string
#    * hated foods list, a list of names of food they don't like
#    * loved foods list, a list of names of food they really do like
#
# Behavior:
#    * taste(food name)  * returns None if the food name is not in their
#                                  hated or loved food lists
#                        * returns True if the food name is in their
#                                  loved food list
#                        * returns False if the food name is in their
#                                  hated food list
#
# Example:
#    person = Person("Malik",
#                    ["cottage cheese", "sauerkraut"],
#                    ["pizza", "schnitzel"])
#
#    print(person.taste("lasagna"))     # Prints None, not in either list
#    print(person.taste("sauerkraut"))  # Prints False, in the hated list
#    print(person.taste("pizza"))       # Prints True, in the loved list
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

class Person:
    def __init__(self, name, hate, love):
        self.name = name
        self.hate = hate
        self.love = love

    def taste(self, food):
        if food in self.hate:
            return False
        elif food in self.love:
            return True


# Init instance
instance = Person("Malik", ["cottage cheese", "sauerkraut"], ["pizza", "schnitzel"])

# Invoke method and print
print(instance.taste("lasagna"))
print(instance.taste("sauerkraut"))
print(instance.taste("pizza"))
