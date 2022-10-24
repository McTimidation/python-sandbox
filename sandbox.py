def cube(x): print(x*x*x)
cube(10)

class Car:
    def __init__(self, input_model):
        self.model = input_model
        self.mileage = 0
    def vrooom(self, distance):
        self.mileage += distance
    def __str__(self):
        output = f"Hello, I am a {self.model} and I have traveled {self.mileage} miles"
        return output

myHonda = Car("Honda")
print(myHonda.mileage)


