from abc import abstractmethod, ABCMeta
from random import randint

class Account(metaclass = ABCMeta):
    @abstractmethod
    def __init__():
         return 0
    @abstractmethod
    def create_acc():
        return 0
    @abstractmethod
    def authenticate():
        return 0
    @abstractmethod
    def withdraw():
        return 0
    @abstractmethod
    def deposit():
        return 0
    @abstractmethod
    def display_balance():
        return 0

class SavingsAccount(Account):
    def __init__(self):
        #[key][0] =>name : [key][1] => balance
        self.savings_account = {}

    def create_acc(self,name, initial_deposit):
        self.account_num = randint(10000, 99999)
        self.savings_account[self.account_num] = [name, initial_deposit]
        print("Account created succesfully, your account number is: ",
            self.account_num)

    def authenticate(self, name, account_num):
        if account_num in self.savings_account.keys():
            if self.savings_account[account_num][0] == name:
                print("Authentication successful")
                self.account_num = account_num
                return True
            else: 
                print("Athentication Failed!")
                return False
        else: 
            print("Athentication Failed!")
            return False
    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.savings_account[self.account_num][1]:
            print("Insufficient Funds")
        else:
            self.savings_account[self.account_num][1] -= withdraw_amount
            print("withdrawal succesful")
            self.display_balance()

    def deposit(self, deposit_amount):
        self.savings_account[self.account_num][1] += deposit_amount
        print("Deposit was succesful!")
        self.display_balance()
    def display_balance(self):
        print("Your balance is: ", self.savings_account[self.account_num][1])

savingsaccount = SavingsAccount()
while True:
    print("Enter 1 to Create a new account")
    print("Enter 2 to log into existing Account")
    print("Enter 3 to exit")
    user_input = int(input())
    if user_input == 1:
        print("Enter your Name: ")
        name = input()
        print("Enter your initial deposit: ")
        deposit = int(input())
        savingsaccount.create_acc(name, deposit)
    elif user_input == 2:
        print("Enter your Name: ")
        name = input()
        print("Enter your Account Number: ")
        account_num = int(input())
        authenticate_status = savingsaccount.authenticate(name, account_num)
        if authenticate_status == True:
            while True:
                print("enter 1 to withdraw")
                print("enter 2 to deposit")
                print("enter 3 to display avaialable balance")
                print("enter 4 to return to previous menu")
                user_choice = int(input())
                if user_choice == 1:
                    withdraw_amount = int(input("please enter withdrawal amount: "))
                    savingsaccount.withdraw(withdraw_amount)
                elif user_choice == 2:
                    deposit_amount = int(input("Please enter deposit amount: "))
                    savingsaccount.deposit(deposit_amount)
                elif user_choice == 3:
                    savingsaccount.display_balance()
                elif user_choice == 4:
                    break
    elif user_choice == 3:
        quit()