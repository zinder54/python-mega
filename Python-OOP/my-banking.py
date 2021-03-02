from random import randint

class PersonalBank:
    def __init__(self):
        self.bank_name = {}
        self.bank_name[self.acc_num] = [name, initial deposit]
        

class CurrentClient(PersonalBank):
    def sign_in(self, acc_num):
        print("please enter your name and account number to sign in")
        self.name = input("Name: ")
        if self.name in self.bank_name:
            input("Account Number: ")
        else:
            print("Sorry we do not recognise that name")
            print("\n maybe you would like to open an account?")
        
        
class NewClient:
    def setup(self, name, initial_deposit):
        print("please fill in the answers below to open your new account")
        name = input("Please enter your name: ")
        initial_deposit = input("Please enter the amount you wish to deposit: ")
        self.acc_num = randint(10000,99999)
        print("Thankyou for setting up your account, your new account number is: ", self.acc_num)

currentclient = CurrentClient()
newclient = NewClient()

print("enter 1 if you are a returning customer")
print("enter 2 if you are a new customer")
user_choice = int(input())
if user_choice == 1:
    newclient.sign_in()
if user_choice == 2:
    newclient.setup()
