# bissextile year


class SimpleNumbersIterator:

    def __init__(self, quantity_simple_numbers):

        self.quantity_simple_numbers = quantity_simple_numbers
        self.__quantity_returned = 0
        self.__cur_num = 2


    def __iter__(self):
        return self

    def __next__(self):

        if self.__quantity_returned == self.quantity_simple_numbers:
            raise StopIteration

        self._get_simple_number()
        self.__quantity_returned = self.__quantity_returned + 1
        return self.__cur_num


    def _get_simple_number(self):

        while True:
            self.__cur_num += 1
            if self._is_prime(self.__cur_num):  # просте число знайдено
                return self.__cur_num


    def _is_prime(self, number):

        for k in range(2, number - 1):
            if number % k == 0:
                return False
        return True


lsit_of_simple_numbers = list(SimpleNumbersIterator(15))
print(lsit_of_simple_numbers)

