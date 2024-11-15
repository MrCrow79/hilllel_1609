class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass  # Абстрактний метод


    def __setattr__(self, key, value):
        if key == 'name':
            if len(value) == 0:  # мати хоча б 1 символ
                print('You cant user name ="" ')
                return

        super().__setattr__(key, value)


class Mammal(Animal):
    def __init__(self, name, num_legs):
        # super().__init__(name)
        Animal.__init__(self, name)
        self.num_legs = num_legs


    def __setattr__(self, key, value):

        if key == 'num_legs':
            if value < 1 :
                print('At least 1 leg')
                return
        super().__setattr__(key, value)


class Bird(Animal):
    def __init__(self, name, wingspan):
        # super().__init__(name)
        Animal.__init__(self, name)
        self.wingspan = wingspan


class Bat(Mammal, Bird):  # Ромбовидне наслідування
    def __init__(self, name, num_legs, wingspan):
        Mammal.__init__(self, name, num_legs)
        Bird.__init__(self, name, wingspan)

    def sound(self):
        return "Squeak"  # Звук кажана

# mam = Mammal("", 1)
# print(mam.name)
# print(mam.num_legs)

print(Mammal.mro())
# print('Mammal', Mammal.mro())
# print('Bird', Bird.mro())
# print('Bat', Bat.mro())


# Створення об'єкту класу Bat

#
# # Виведення атрибутів об'єкту bat
# print("Назва:", bat.name)
# print("Кількість ніг:", bat.num_legs)
# print("Розмах крил:", bat.wingspan)
#
# # Виклик методу sound для об'єкту bat
# print("Звук:", bat.sound())

