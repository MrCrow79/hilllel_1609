class Car:

    class_name = 'Car'  # attribute, як змінна

    def __init__(self, brand, model):  # метод, як функція

        self.brand = brand
        self.model = model
        self.tank = 0  #  1 км на літр


    def go_somewhere(self, amount_in_km):  #

        if self.tank >= amount_in_km:  # інкапсуляція
            self.tank = self.tank - amount_in_km
            print('Driving...')
        else:
            print('Can\'t go - have not enougth fuel')


    def set_tank(self, value):  # метод, як функція

        self.tank = value


x5 = Car(brand='BMW', model='X5')  # instance, екземпляр

print(x5.class_name)
print(x5.model)
print(x5.brand)
print(x5.tank)
x5.set_tank(50)
x5.tank = 50

x5.go_somewhere(40)
x5.go_somewhere(40)

# print(x5.tank)
#
# print('-'*80)
#
# polo = Car(brand='VW', model='polo')  # instance, екземпляр
#
# print(polo.class_name)
# print(polo.model)
# print(polo.brand)
# print(polo.tank)