class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

d1 = Dog("rex")
d1.speak()