class Filters:
    # ?age_gte=20&score_lte=40

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)  # self.age_gte = 20, setattr(об'єкт, ім'я атрибути, значення атрибута)

    def __eq__(self, other):
        for k in [k for k in self.__dict__ if k is not None]:  # всі поточні атрибути які не None

            if self.__dict__[k] != getattr(other, k, None):  # кожний поточний атрибут == атрибуту в іншому фільтрі
                return False

        return True

f1 = Filters(**{'age_gte': 20, 'score_lte': 40})
f2 = Filters(**{'age_gte': 20, 'score_lte': 40, 'some': None})

print(f1 == f1)
print(f1 == f2)