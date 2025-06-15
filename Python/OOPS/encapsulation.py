class BankAccount:
    def __init__(self):
        self.__balance = 0  # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

# acc:BankAccount = BankAccount()   -> this way of object making is also correct
acc = BankAccount()
acc.deposit(1000)
print(acc.get_balance())  # 1000
# print(acc.__balance)    # ❌ Will give error

# Data Hiding -> data can only be accessible to some authentic persons