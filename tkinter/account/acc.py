class Account: #class

    def __init__(self, filepath):
        self.filepath=filepath #instance variable
        with open(filepath, 'r') as file:
            self.balance=float(file.read())

    def withdraw(self,amount):
        self.balance=self.balance - amount

    def deposit(self, amount):
        self.balance=self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):#inheritance, created a subclass of Account and shares methods
    """this class generates checking objects...and this is a docstring"""
    type="checking"#class variable

    def __init__(self,filepath,fee): #constructor
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self, amount): #method
        self.balance=self.balance - amount - self.fee


jacks_checking=Checking("balance.txt", 1) #object instance, stores data in the txt file
                                            #also an instantiation of the class
jacks_checking.transfer(10)
print(jacks_checking.balance)
jacks_checking.commit()
print(jacks_checking.type)

phil_checking=Checking("phil.txt",1) #same as jacks, object instance and instantiation of class
phil_checking.transfer(10)
print(phil_checking.balance)
phil_checking.commit()
print(phil_checking.__doc__)
