#encapsulation: protecting data inside a class
# - keeping attributes and methods private, so they cannot be accessed directly from outside the class
#helps prevent accidental changes
#use __ make properties private
#use getter method to access private properties
#example

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade

    def get_grade(self):
        return self.__grade

s1 = Student("Aryan", "A*")
print(s1.get_grade())

#setter method: helps modify private properties
#exmaple:
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade

    def get_grade(self):
        print(self.__grade)

    def set_grade(self, grade):
        self.__grade = grade

s1 = Student("Aryan", "A*")
s1.get_grade()
s1.set_grade("A")
s1.get_grade()


        
    