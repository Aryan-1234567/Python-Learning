#methods are a function which is created inside a class
#methods can accept parameters and can return values
#example:
class Calculator:
    def __init__ (self, num1, num2):
        self.num1 = num1
        self.num2 = num2   

    def add(self):
        return self.num1 + self.num2

c1 = Calculator(10, 20)
print(c1.add())
