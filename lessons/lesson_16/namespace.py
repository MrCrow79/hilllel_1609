# global
# non-local
# local

global_variable = 'Global var'
dog_name = 'Alex'

def dog_actions(name):

    dog_name = name  # non-local var

    def make_sound():

        global dog_name

        dog_name = 'Den'

        # dog_name = 'Richi'
        dogs_sound = 'Rrrrr'  # local war
        print(dogs_sound)
        print(dog_name)  # 1

    def walk():
        print('waking')

    walk()
    make_sound()
    print(dog_name)  # 2


dog_actions('Naida')
print(dog_name) # 3
