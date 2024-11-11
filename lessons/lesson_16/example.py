"""Опишіть об’єкт «Поїзд». Клас повинен містити поля та метод для додавання вагонів
(необхідно додати об’єкти та екземпляри класу вагонів).

В поїзді завжди є 1 вагон і це локомотив(він не приймає пасажирів)
Опишіть клас Вагон разом із поїздом. Вагон повинен містити список пасажирів і дозволяти додавати пасажирів.
У Вагоні може бути не більше 10 пасажирів.

Під час використання функції len у вагоні я хочу бачити кількість пасажирів.
Використовуючи len у поїзді, я хочу бачити список вагонів без локомотива. Кожен вагон повинен мати номер.
"""

class Wagon:
    max_pass = 10  # class var

    def __init__(self, number: int = None, is_locomotive: bool = False):

        if number is None and not is_locomotive:
            raise AssertionError('You have to put wagon number')

        if is_locomotive:
            number = 0

        self.number = number
        self.is_locomotive = is_locomotive
        self.list_of_pass = []

    def add_pass(self, new_pass: dict):
        if self.is_locomotive:
            return

        if len(self.list_of_pass) < 10:
            self.list_of_pass.append(new_pass)


    def __len__(self):
        return len(self.list_of_pass)


    def __str__(self):
        return f'Wagon #{self.number}'


class Train:

    def __init__(self):
        self.locomotive = Wagon(number=1, is_locomotive=True)
        self.wagons = []

    def add_wagon(self, number: int = None):
        if number is None:
            number = len(self.wagons)

        while number in [k.number for k in self.wagons]:
            number += 1
        wagon = Wagon(number=number)
        self.wagons.append(wagon)


    def __len__(self):
        return len(self.wagons)


    def __add__(self, wagon: Wagon):
        self.wagons.append(wagon)


    def __str__(self):
        return f'Train with {len(self.wagons)} waggons: {", ".join([str(k) for k in self.wagons])}'


    def quantity_of_waggons(self):
        return len(self.wagons)




if __name__ == '__main__':
    train = Train()

    print('Train, main wagon is locomotive:', train.locomotive.is_locomotive)
    print('List of wagons:', train.wagons)
    train.add_wagon(number=2)
    train.add_wagon(number=3)
    train.add_wagon(number=777)
    train.add_wagon()
    print('Train description: ', train)

    wg = Wagon(number=10)
    wg.add_pass({'id': 1, 'name': 'Denys'})
    print('Train description 1: ', train)
    train + wg  # == train.__add__(wg)
    print('Train description 1: ', train)
    print(train.wagons[-1].list_of_pass)



