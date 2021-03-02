class Car: 
    number_of_wheels = 4
    _colour = "black"
    __year_of_manufacture = 2017 #python sees this as _Car__year_of_manufacture

class Bmw(Car):
    def __init__(self):
        print("protected attribute colour: ", self._colour)


car = Car()
print("Public attribute number of wheels: ", car.number_of_wheels)
bmw = Bmw()
print("public attribute year of manufacture: ", car._Car__year_of_manufacture)
#print("public attribute year of manufacture: ", car.__year_of_manufacture)
#^this creates an attribute error because starting with __ stops it from being used outside of class