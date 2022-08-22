# Write four classes that meet these requirements.
#
# Name:       Animal
#
# Required state:
#    * number_of_legs, the number of legs the animal has
#    * primary_color, the primary color of the animal
#
# Behavior:
#    * describe()       # Returns a string that describes that animal
#                         in the format
#                                self.__class__.__name__
#                                + " has "
#                                + str(self.number_of_legs)
#                                + " legs and is primarily "
#                                + self.primary_color
#
#
# Name:       Dog, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Bark!"
#
#
#
# Name:       Cat, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Miao!"
#
#
#
# Name:       Snake, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Sssssss!"

class Animal:
    def __init__(self, number_of_legs, primary_color):
        self.number_of_legs = number_of_legs
        self.primary_color = primary_color

    def describe(self):
        return(self.__class__.__name__ + " has "
            + str(self.number_of_legs)
            + " legs and is primarily "
            + self.primary_color)  # returns class name

class Dog(Animal):
    # don't need dunder init because we already have access to self from Animal class; linked via passing Animal as a param for Dog class
    # super() to extend something from parent class to child class
    # Dog has access to describe AND init from Animal
    # def __init__(self, number_of_legs, primary_color):
    #     super().__init__(number_of_legs) # if you wanted to control which args pass through to this class
    # super() also used for multiple inheritance

    def speak(self):
        return "Bark!"


class Cat(Animal):
    def speak(self):
        return "Miao!"


class Snake(Animal):
    def speak(self):
        return "Ssssss!"


# Init instance
animal = Animal(6, "green")
dog = Dog(4, "white")
cat = Cat(4, "orange")
snake = Snake(0, "black")

# Invoke method and print
print(animal.describe())
print(dog.describe())
print(cat.describe())
print(snake.describe())
