class User:

    def __init__(self, name: str, score: int):

        self.name = name
        self.score = score

    def __str__(self):
        return f'User:{self.name}, score: {self.score}'

    def __setattr__(self, key, value):
         if key == 'score':
             if not (100 >= value >= 0):
                 print(f'score must be between 0 and 100. Set 0')
                 value = 0
         super().__setattr__(key, value)  # викликає метод __setattr__ у батька(object)


den = User('Den', -5)
# den = User('Den', -5)
#
den.score = 100000000
#
print(den)
