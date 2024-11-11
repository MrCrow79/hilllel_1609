from abc import ABC, abstractmethod


# Абстрактний клас тварини
class Animal(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

# Абстрактний клас тварини
class AnimalAlternative:

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        raise NotImplemented('Not implemented make_sound method')

# Клас собаки, що успадковує абстрактний клас Animal
class Dog(Animal):

    @abstractmethod
    def make_sound(self):
        pass

# Клас кота, що успадковує абстрактний клас Animal
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

base_animal = Dog('Ivan')
# base_animal.make_sound()

