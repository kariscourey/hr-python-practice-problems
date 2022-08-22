# Modify the withdraw method of BankAccount so that the bank
# account can not have a negative balance.
#
# If a person tries to withdraw more than what is in the
# balance, then the method should raise a ValueError.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        # If the amount is more than what is in
        # the balance, then raise a ValueError

        if amount > self.balance:
            raise ValueError

        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


instance = BankAccount(100)

# Invoke method and print
print(instance.get_balance())    # Prints 100
instance.deposit(80)
print(instance.get_balance())    # Prints 180
instance.withdraw(200)
print(instance.get_balance())    # Raises ValueError
