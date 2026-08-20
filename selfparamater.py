#self paramater is used to access properties and methods of a class in python
#example:
class Person:
    def __init__(self, height, weight):  #self paramater must be first of any class
        self.height = height
        self.weight = weight

    def body(self):
        print(f'my height is {self.height} and my weight is {self.weight}')

aryan = Person(5.11,65)
aryan.body()