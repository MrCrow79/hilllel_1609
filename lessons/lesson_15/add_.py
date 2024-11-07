class Classes:

    def __init__(self, **kwargs):

        for k,v in kwargs.items():
            setattr(self, k, v)

    # def __add__(self, obj):
    #
    #     for k,v in obj.__dict__.items():
    #         setattr(self, k, v)

    def __add__(self, obj):  # a + b
        x = Classes()

        for k, v in obj.__dict__.items():  # x = Classes(**obj.__dict__.items())
            setattr(x, k, v)

        for k, v in self.__dict__.items():
            setattr(x, k, v)

        return x

    def __str__(self):
        res = f'current_classes is\n'

        for k,v in self.__dict__.items():
            res += f'{k} has studens: {v["students"]}, start at {v["start"]}\n'
            setattr(self, k, v)
        return res


# Використання оператора додавання та автоматичний виклик __add__
basic_classes = Classes(**{
    'math': {'hours': 100, 'students': 20, 'start': '20.05.2023'},
    'phil': {'hours': 30, 'students': 30, 'start': '21.05.2023'},
})

basic_classes = Classes(
    math={'hours': 100, 'students': 20, 'start': '20.05.2023'},
    phil={'hours': 30, 'students': 30, 'start': '21.05.2023'}
)

print('basic')
print(basic_classes)
print('-'*80)

print(basic_classes.math)
print(basic_classes.phil)


extra_classes = Classes(**{
    'biologic': {'hours': 15, 'students': 5, 'start': '30.05.2023'},
})
new_classes = basic_classes + extra_classes
new_classes = basic_classes.__add__(extra_classes)
print('basic')
print(basic_classes)
print('-'*80)
print('new_classes')
print(new_classes)



