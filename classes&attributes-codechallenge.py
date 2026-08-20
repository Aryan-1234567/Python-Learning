#testing my knowledge of classes and attributes in python by doing a small challenge

class Person:   #creating a class called person
    def __init__(self, name, age):  #using the __init__constructor method to initialise attributes of name and age
        self.name = name    #creating attribute name and giving it a value of name
        self.age = age      #creating attribute age and giving it a value of age

def greet(self):    #creating a function called greet that takes self as a parameter
    print(f"Hello, my name is {self.name}")     #prints a greeting message using the name attribute of the object

    p1 =Person("John", "36")    #created an object called p1 of class Person and passed values of John and 36 to attribues

    p1.greet()      #calls greet function of p1 and prints greeting message using attribues of the object p1


