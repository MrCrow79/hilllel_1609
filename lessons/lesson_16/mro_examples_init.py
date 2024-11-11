class Animal():

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print('animl sound')


class Lion(Animal):

    def __init__(self, name):
        super().__init__(name) # Lion.__init__(self, name)
        self.legs = 4
        self.color = 'Orange'

    def make_sound(self):
        super().make_sound()
        print('by Lion version')


class Bird(Animal):

    def __init__(self, name):
        super().__init__(name)
        self.wings = 2
        self.color = 'Grey'


class Pterozawr(Lion, Bird):

    def __init__(self, name):

        Bird.__init__(self, name)
        Lion.__init__(self, name)

    def make_sound(self):
        super(Lion, self).make_sound()  #$ --> Animal.make_sound(self)
        print('by Pterozawr version')


pt = Pterozawr('Alex')
print(pt.legs)
print(pt.wings)
print(pt.color)
pt.make_sound()




