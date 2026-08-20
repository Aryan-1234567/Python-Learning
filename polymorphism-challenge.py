class Cat:
    def sound(self):
        print ("Meow")

class Fox:
    def sound(self):
        print("Wa-pa-pa-pa-pa-pow")

c1 = Cat()
f1 = Fox()

for x in (c1, f1):
    x.sound()
        