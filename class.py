class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 5

# Create an instance of the Car class
my_car = Car(make="Toyota", model="Camry")

# Access attributes
print(f"Make: {my_car.make}, Model: {my_car.model}")

# Call methods
my_car.accelerate()
print(f"Current Speed: {my_car.speed}")

# Create another instance
your_car = Car(make="Ford", model="Mustang")
