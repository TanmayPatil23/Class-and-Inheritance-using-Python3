import turtle as t

class shapes:
    def __init__(self, sides = 0, side_length = 0):
        self.side_length = side_length
        self.sides = sides
class regular_shape(shapes):
    def isRegular(self):
        print(True)

#shape 1 - triangle
class triangle(regular_shape):
    def define(self):
        print("Triangle is shape with three sides")
    def draw(self):
        for i in range(self.sides):
            t.forward(self.side_length)
            t.right(60)

#shape 2 - square
class square(regular_shape):
    def define(self):
        print("Square is shape with four equal side lengths")
    def draw(self):
        for i in range(self.sides):
            t.forward(self.side_length)
            t.right(90)

#shape 3 - pentagon
class pentagon(regular_shape):
    def define(self):
        print("Regular pentagon is shape with five equal side lengths")
    def draw(self):
        for i in range(self.sides):
            t.forward(self.side_length)
            t.right(72)


#shape 5 - star
class star(regular_shape):
    def draw(self):
        for i in range(self.sides):
            t.forward(self.side_length)
            t.right(135)

#shape 6 - circle
class circle:
    def __init__(self, radius = 0):
        self.radius = radius
    def draw(self):
        t.circle(self.radius)

c = circle(50)
c.draw()
t.reset()
s = square(4, 50)
s.draw()
t.reset()
p = pentagon(5, 50)
p.draw()
t.reset()
sr = star()
sr.draw(8, 50)
t.reset()





