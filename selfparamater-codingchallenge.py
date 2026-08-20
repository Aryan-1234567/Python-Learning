class Cars:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print(f'the brand of the car is {self.brand}')

c1 = Cars("Ford")
c1.show()
