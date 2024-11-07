
class Car:
    def __init__(self, make, model, tank=50, coef=0.2, full_price=35000):
        self.make = make
        self.tank = tank
        self.full_price = full_price
        self.model = model
        self.__year = 2022
        self._coef = coef
        self.__price_coef = 0.9


    def set_year(self, year):

        if year > self.__year:
            print('You can\'t make your car yanger')
            return
        self.__year = year


    def get_year(self):
        return self.__year


    @property  # getter, property
    def year(self):
        return self.__year


    @year.setter  # setter for year property. cant be created without row 25-26:
    def year(self, value):

        if value > self.__year:
            print('You can\'t make your car yanger')
            return
        self.__year = value


    @property
    def current_time(self):
        import datetime
        return datetime.datetime.now()


car = Car('tesla', 'x3')

# car.set_year(2024)
# print(car.get_year())

print(car.year)
print(car.current_time)

car.year = 2024
car.year = 2021

print(car.year)