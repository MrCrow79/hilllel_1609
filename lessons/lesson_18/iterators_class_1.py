# bissextile year


class SimpleRangeIterator:

    def __init__(self, max_number):

        self.__current = -1
        self.max_number = max_number


    def __iter__(self):
        return self

    def __next__(self):

        if self.__current == self.max_number:
            raise StopIteration

        self.__current = self.__current + 1
        return self.__current


class IteratorWithoutStop:

    def __init__(self):
        self.__current = -1


    def __iter__(self):
        return self

    def __next__(self):
        self.__current = self.__current + 1
        return self.__current


# iter_10 = iter(SimpleRangeIterator(10))
# iter_20 = SimpleRangeIterator(20).__iter__()
#
# next(iter_10)
# next(iter_20)

#
# try:
#     iter_15 = iter(SimpleRangeIterator(15))
#     while True:
#         print(next(iter_15))
# except StopIteration:
#     pass
#
# for number in SimpleRangeIterator(15):
#     print(number)


# counter = 1000
#
# for _ in SimpleRangeIterator(-2):
#     if counter == 0:
#         break
#     counter = counter - 1
#     print(_)