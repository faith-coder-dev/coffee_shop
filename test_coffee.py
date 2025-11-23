from customer import Customer
from coffee import Coffee
from order import Order


def test_coffee_creation():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_coffee_orders_and_customers():
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    coffee = Coffee("Mocha")
    order1 = Order(customer1, coffee, 5.0)
    order2 = Order(customer2, coffee, 6.0)
    assert order1 in coffee.orders()
    assert customer1 in coffee.customers()
