#polymorphism: methods/fuinctions/operators with same bname which can be executed on classes and objects
#of different types

#example:

class Car:
    def __init__(self, model):
        self.model = model

    def move(self):
        print("The car is moving on the road.")

class Aeroplane:
    def __init__(self, model):
        self.model = model

    def move(self):
        print("The aeroplane is flying in the sky.")

class Ship:
    def __init__(self, model):
        self.model = model

    def move(self):
        print("The ship is sailing in the water.")

c1 = Car("Toyota")
a1 = Aeroplane("Boeing")
s1 = Ship("Titanic")

for y in (c1, a1, s1):     #for loop to execute all the move methods of different classes
    y.move()