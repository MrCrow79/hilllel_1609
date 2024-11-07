class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __del__(self):
        print(f"The {self.make} {self.model} object has been destroyed.")

a = 5
my_car = Car('', '2')

# del my_car  #  my_car.__del__()  нищення об'єкта та автоматичний виклик деструктора
