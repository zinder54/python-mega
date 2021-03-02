class Employee:
    def number_of_work_hours(self):
        self.number_of_work_hours = 40
    
    def display_number_of_work_hours(self):
        print(self.number_of_work_hours)

class Trainee(Employee):
    def number_of_work_hours(self):
        self.number_of_work_hours = 45
    def reset_working_hours(self):
        super().number_of_work_hours()#super overrides any other variable of same name and, 
        #resets to the original variable object


employee = Employee()
employee.number_of_work_hours()
print("number of work hours for employee: ", end=' ')#end='' makes it the line isnt broken and ,
#40 is on same line
employee.display_number_of_work_hours()
trainee = Trainee()
trainee.number_of_work_hours()
print("number of work hours for trainee: ", end=' ')
trainee.display_number_of_work_hours()
trainee.reset_working_hours()
print("number of work hours for trainee after reset: ", end=' ')
trainee.display_number_of_work_hours()