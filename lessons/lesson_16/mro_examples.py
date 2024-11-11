class Animal():

    def walk(self):
        print('walking..')

    def make_sound(self):
        print('animl sound')


class Lion(Animal):

    def make_sound(self):
        print('Rrrrr')


class Bird(Animal):

    def walk(self):
        print('fly... somewhere')

    def make_sound(self):
        print('Chirick')

class Pterozawr(Lion, Bird):
    pass

zavr = Pterozawr()

zavr.make_sound()
zavr.walk()

print(Pterozawr.mro())

# small_lion = Lion()
#
# small_lion.walk()
# small_lion.make_sound()
#
# callibri = Bird()
# callibri.walk()


