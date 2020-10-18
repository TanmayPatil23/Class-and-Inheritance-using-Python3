class animals:
    def __init__(self, legs = 4, eyes = 2):
        self.legs = legs
        self.eyes = eyes

class wild(animals):
    def livein(self):
        print("Lives in forests")

class domestic(animals):
    def livein(self):
        print("Domesticated shelters provided by humans")

# Animal 1 - cat

class cat(domestic):
    def sound(self):
        print("Meow")
    def feeds_on(self):
        print("Milk, sometimes mice")
    def avg_age(self):
        print(2, " to ", 16, " years")
# Animal 2 - dog

class dog(domestic):
    def sound(self):
        print("Barks")
    def feeds_on(self):
        print("I feed them Pedigree")
    def avg_age(self):
        print(10, " to ", 13, " years")
# Animal 3 - cow

class cow(domestic):
    def sound(self):
        print("Moos")
    def feeds_on(self):
        print("Fodder")
    def avg_age(self):
        print(18, " to ", 22, " years")
# Animal 4 - goat

class goat(domestic):
    def sound(self):
        print("Bleats, which is \'maa\' indeed")
    def feeds_on(self):
        print("Grass or Fodder")
    def avg_age(self):
        print(15, " to ", 18, " years")
# Animal 5 - donkey

class donkey(domestic):
    def sound(self):
        print("Hee - haw, sounds funny!")
    def feeds_on(self):
        print("Hay")
    def avg_age(self):
        print(25, " to ", 30, " years")
# Animal 6 - lion

class lion(wild):
    def sound(self):
        print("Roars")
    def feeds_on(self):
        print("Flesh of hunted animals")
    def avg_age(self):
        print(10, " to ", 14, " years")
# Animal 7 - monkey

class lion(wild):
    def sound(self):
        print("Gibbers")
    def feeds_on(self):
        print("Fruits and nuts")
    def avg_age(self):
        print("Depends on the species of monkey")
# Animal 8 - giraffe

class giraffe(wild):
    def sound(self):
        print("Humms")
    def feeds_on(self):
        print("Leaves of trees")
    def avg_age(self):
        print(20, " to ", 25, " years")
# Animal 9 - elephant

class elephant(wild):
    def sound(self):
        print("Trumpets")
    def feeds_on(self):
        print("Barks of trees")
    def avg_age(self):
        print("Around 48 years")
# Animal 10 - horse

class horse(wild):
    def sound(self):
        print("Neighs")
    def feeds_on(self):
        print("Grass or Hay")
    def avg_age(self):
        print(25, " to ", 30, " years")


lido = dog()
print("Lido has", lido.eyes, "eyes")
print("Lido has", lido.legs, "legs")
print("Lives in", end = " ")
lido.livein()
print("Feeds on", end = " ")
lido.feeds_on()
print("Has an average life of", end = " ")
lido.avg_age()
print("Sound :", end = " ")
lido.sound()