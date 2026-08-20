#inheritance: a class can be defined to inherits all the properties and methods of another class
#parent class: the class which is inherited from
#child class: the class which inherits from another class

#example:

class Teacher:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}"

class Student(Teacher):
    def __init__(self, name, grade):
        super().__init__(name)              #super(). inherits the properties and methods of the parent class
        self.grade = grade

    def greet(self):
        return f"Hello, my name is {self.name} and I am in grade {self.grade}"      #overriding the greet method of the parent class

s1 = Student("John", 10)
print(s1.greet())
