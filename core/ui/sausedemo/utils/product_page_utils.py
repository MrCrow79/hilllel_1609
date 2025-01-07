from enum import Enum


class ProductPageSorting(Enum):

    NAME_ASK = 'Name (A to Z)'
    NAME_DESC =  'Name (Z to A)'
    PRICE_ASC =  'Price (low to high)'
    PRICE_DESC =  'Price (high to low)'


def get_reverse_by_sorting(sorting_type: ProductPageSorting):

    return {
        ProductPageSorting.NAME_ASK: False,
        ProductPageSorting.NAME_DESC: True,
        ProductPageSorting.PRICE_ASC: False,
        ProductPageSorting.PRICE_DESC: True,
    }[sorting_type]