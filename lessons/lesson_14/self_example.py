class Auto:

    def __init__(self, model, color, engine, fuel_to_km=0.2):  # конструктор, magic method
        self.model = model
        self.color = color
        self.engine = engine

        self.tank = 0   # default value, can't change

        self.__fuel_to_km = fuel_to_km


    def drive_to_nearest_town(self, distance_km):

        if self.tank / self.__fuel_to_km >= distance_km:
            self.tank = self.tank - distance_km * self.__fuel_to_km

            print('driving..')
        else:
            print(f'Can go there, have fuel only on {self.tank / self.__fuel_to_km}')


class Nissan(Auto):

    brand = 'NISSAN'  # class attribute
    BASE_COUNTRY = 'JAPAN'  # class attribute

    @classmethod
    def say_greetings(cls):
        print(f'Hello from {cls.brand}')

    @classmethod
    def get_base_country(cls):
        return cls.BASE_COUNTRY


    def say_greetings_not_class_method(self):
        print(f'Hello from {self.brand}')


y61 = Nissan(model='y61', color='Green', engine='3.0', fuel_to_km=0.1)  # інстанс = екземляр класу
navara = Nissan(model='navara', color='Black', engine='5.2')


print(navara.BASE_COUNTRY)
Nissan.BASE_COUNTRY = 'Ukraine' # змінив змінну класа
print(Nissan.get_base_country())
# Nissan.say_greetings_not_class_method()  не працює
navara.say_greetings_not_class_method() # == Nissan.say_greetings_not_class_method(navara)
Nissan.say_greetings_not_class_method(navara)

print(navara.BASE_COUNTRY)


# y61.tank = 50
#
# y61.drive_to_nearest_town(400)
# y61.drive_to_nearest_town(400)


# y61_2 = Nissan(model='y61', color='Green', engine='3.0')  #
#
# y61_2.tank = 50  # 250 km
#
# y61_2.drive_to_nearest_town(400)
# y61_2.drive_to_nearest_town(400)


# y61_2 = Nissan(model='y61', color='Green', engine='3.0')
# navara = Nissan(model='navara', color='Black', engine='5.2')



#
# print(id(y61))
# print(id(y61_2))
#
# y61.color = 'Red'
#
# print(id(y61))
# print(id(y61_2))
#
# print(y61.color)
# print(y61_2.color)
# print(y61_2.brand)