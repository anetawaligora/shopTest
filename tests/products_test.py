import pytest

from pages import ProductsPage, ProductsSorting


@pytest.mark.usefixtures("setup")
class TestProductsPage:

    def prepare_products_page(self):
        cart_page = ProductsPage(self.driver)
        cart_page.open_page()
        cart_page.log_in()

        return cart_page

    def test_cart_without_products(self):
        cart_page = self.prepare_products_page()

        assert cart_page.is_cart_badge_displayed() is False

    def test_add_single_product_to_cart(self):
        cart_page = self.prepare_products_page()
        cart_page.add_to_cart(0)

        assert cart_page.is_cart_badge_displayed() is True
        assert '1' == cart_page.get_cart_badge_count()

    def test_add_multiple_product_to_cart(self):
        expected_count = 4

        cart_page = self.prepare_products_page()

        for index in range(expected_count):
            cart_page.add_to_cart(index)

        assert cart_page.is_cart_badge_displayed() is True
        assert str(expected_count) == cart_page.get_cart_badge_count()

    def test_add_and_remove_product(self):
        product_index = 0

        cart_page = self.prepare_products_page()
        cart_page.add_to_cart(product_index)
        cart_page.remove_from_cart(product_index)

        assert cart_page.is_cart_badge_displayed() is False

    def test_verify_default_sorting(self):
        expected_default_sorting = ProductsSorting.az.value.upper()

        cart_page = self.prepare_products_page()
        assert cart_page.get_active_sort_option() == expected_default_sorting

    def test_change_sorting(self):
        cart_page = self.prepare_products_page()

        for products_sorting in list(ProductsSorting):
            cart_page.change_sorting_type(products_sorting)
            assert cart_page.get_active_sort_option() == products_sorting.value.upper()

    def test_price_low_to_high(self):
        cart_page = self.prepare_products_page()
        cart_page.change_sorting_type(ProductsSorting.lohi)
        prices = cart_page.get_products_prices_in_display_order()

        assert prices == sorted(prices)

    def test_price_high_to_low(self):
        cart_page = self.prepare_products_page()
        cart_page.change_sorting_type(ProductsSorting.hilo)
        prices = cart_page.get_products_prices_in_display_order()

        assert prices == sorted(prices, reverse=True)

    def test_name_sorting_alphabetically(self):
        cart_page = self.prepare_products_page()
        cart_page.change_sorting_type(ProductsSorting.az)
        names = cart_page.get_products_names_in_display_order()

        assert names == sorted(names)

    def test_name_sorting_reversed_alphabetically(self):
        cart_page = self.prepare_products_page()
        cart_page.change_sorting_type(ProductsSorting.za)
        names = cart_page.get_products_names_in_display_order()

        assert names == sorted(names, reverse=True)
