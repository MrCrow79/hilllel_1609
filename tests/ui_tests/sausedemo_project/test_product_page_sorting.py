import pytest

from core.ui.sausedemo.product_page_asserts import assert_product_page_is_sorted
from core.ui.sausedemo.utils.product_page_utils import ProductPageSorting, get_reverse_by_sorting


class ProductPageTest:

    def test_product_page_sorting_by_default(self, product_page_session):

        # actual_sorting_text =  product_page_session.get_current_sorting_element().text

        #
        # assert actual_sorting_text == product_page_session.default_sorting_text
        #
        # product_names = [k.text for k in product_page_session.products_names()]
        # product_names_sorted = sorted(product_names)
        # assert product_names_sorted == product_names

        assert_product_page_is_sorted(
            sorting_name=product_page_session.default_sorting_text,
            reverse_option=product_page_session.is_default_sorting_reversed,
            product_page=product_page_session,
        )


    @pytest.mark.parametrize('order_by_value', [*list(ProductPageSorting)])  # *list(ProductPageSorting) == [ProductPageSorting.NAME_ASK, ProductPageSorting.NAME_DESC]
    def test_product_page_sorting_all_options(self, product_page_session, order_by_value):

        option_text = order_by_value.value
        reverse_option = get_reverse_by_sorting(order_by_value)

        product_page_session.select_sorting(option_text)

        assert_product_page_is_sorted(
            sorting_name=option_text,
            product_page=product_page_session,
            reverse_option=reverse_option
        )


