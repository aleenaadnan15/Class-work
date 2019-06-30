class shape():
    def __init__(self,sides,colour):
        self.sides = sides
        self.colour = colour

    def showsides(self):
            print('the sides are' ,self.sides)

    def showcolour(self):
            print('the colour is' ,self.colour)

triangle = shape(3, 'yellow')

triangle.showsides()

triangle.showcolour()

print(triangle.sides)

