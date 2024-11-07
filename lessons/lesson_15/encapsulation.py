

class Car:
    def __init__(self, make, model, tank=50, coef=0.2, full_price=35000):
        self.make = make          # Public attribute
        self._model = model        # Protected attribute
        self.__year = 2022         # Private attribute
        self.tank = tank
        self.full_price = full_price
        self._coef = coef
        self.__price_coef = 0.9

    def some_fn(self):
        self._some_attr = 10

    def cur_quant_of_km(self):
        return self.tank * self._coef

    def current_price_incorrect(self):
        self.__price_coef = 1
        res = round(self.full_price *(pow(self.__price_coef, 2025 - self.__year)), 2)
        self.__price_coef = 0.9
        return res

    def current_price(self):
        return round(self.full_price *(pow(self.__price_coef, 2025 - self.__year)), 2)


car = Car('make_asd', 'model_tesla', coef=0.15, full_price=50000)
# car.some_fn()
#
# car._new_attr = 50

# print(car.make)
# print(car._model)
# print(car.__year)
print(car.current_price())
print(car.current_price_incorrect())
car._Car__price_coef = 10
print(car._Car__price_coef)
print(car.current_price())



# print(car._some_attr)
# print(car._new_attr)


