class Square:
    def __init__(self, side):
        self.side = side
#wihout __add__ python will throw an error because no method within the class for adding the 2 together
    def __add__(,SquareOne, SquareTwo):
        return((4 * SquareOne.side) + (4 * SquareTwo.side))
SquareOne = Square(5) #5 * 4 = 20
SquareTwo = Square(10) #10 * 4 = 40
print("sum of square one and two = ", SquareOne + SquareTwo)
