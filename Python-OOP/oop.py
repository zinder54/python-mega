class Employee:
    def __init__(self, name):#init method initialises the class so self can be used in all methods
        self.name = name
        print("name = ", self.name)
        age = 30 #not adding self here makes it so it cannot be used in any other method.
        print("age = ", age)

    def print_employee_details(self):
        print("printing in another function")
        print("name = ", self.name)
        #print("age = ", age) #will return a name error, not inherited self from other method
    
    @staticmethod #python decorator, skips binding of self
    def welcome_message():
        print("welcome to our organization")

employee = Employee("matthew")   
employeetwo = Employee("dave")
employee.print_employee_details()
employee.welcome_message()