"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from classes.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000) is True
        assert product.check_quantity(999) is True
        assert product.check_quantity(1) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(1000)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии

        with pytest.raises(ValueError):
            assert product.buy(quantity=2000)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        cart.add_product(product, 0)
        assert cart.products[product] == 0
        cart.add_product(product, 100)
        assert cart.products[product] == 100

    def test_remove_product(self, cart, product):
        cart.add_product(product, 1000)
        cart.remove_product(product, 1000)
        assert product not in cart.products
        cart.add_product(product, 999)
        cart.remove_product(product, 100)
        assert cart.products[product] == 899

    def test_clear(self, cart, product):
        cart.add_product(product, 1000)
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 5)
        assert cart.get_total_price() == 500

    def test_buy(self, cart, product):
        cart.add_product(product, 500)
        cart.buy()
        assert product.quantity == 500
        cart.add_product(product, 5000)
        with pytest.raises(ValueError):
            cart.buy()
