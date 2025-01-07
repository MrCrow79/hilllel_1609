def assert_product_page_is_sorted(sorting_name, product_page, reverse_option):

    if 'price' in sorting_name.lower():
        assert_product_page_is_sorted_by_prices(sorting_name, product_page, reverse_option)

    else:
        assert_product_page_is_sorted_by_names(sorting_name, product_page, reverse_option)


def assert_product_page_is_sorted_by_names(sorting_name, product_page, reverse_option):

    assert sorting_name == product_page.get_current_sorting_element().text

    product_names = [k.text for k in product_page.products_names()]
    product_names_sorted = sorted(product_names, reverse=reverse_option)

    assert product_names_sorted == product_names, f'Expected {product_names_sorted} == {product_names}'


def assert_product_page_is_sorted_by_prices(sorting_name, product_page, reverse_option):

    assert sorting_name == product_page.get_current_sorting_element().text

    products_prices = [float(k.text[1:]) for k in product_page.products_prices()]
    products_prices_sorted = sorted(products_prices, reverse=reverse_option)

    assert products_prices_sorted == products_prices, f'Expected {products_prices_sorted} == {products_prices}'