class Animal:

    base_class = 'Animal class asd'

    def make_sound(self):
        print('Animal sound')

    def go_sleep(self):
        print('I go to sleep')


class Dog(Animal):  #  наслідування

    def make_sound(self):  # поліморфізм
        print('Rrrrr')


class Cat(Animal):  #  наслідування

    def make_sound(self):
        print('Miaw')


patron = Dog()  # створення екземпляру класу Dog
lazy_cat = Cat()  # створення екземпляру класу Cat
unknown = Animal()

unknown.go_sleep()
lazy_cat.go_sleep()
patron.go_sleep()

print(patron.base_class)
patron.make_sound()
lazy_cat.make_sound()
unknown.make_sound()

