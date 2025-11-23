import pytest
from customer import Customer
from coffee import Coffee
from order import Order



def test_customer_creation():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_customer_orders_and_coffees():
    customer = Customer("Bob")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Cappuccino")
    order1 = Order(customer, coffee1, 5.0)
    order2 = Order(customer, coffee2, 6.0)
    assert order1 in customer.orders()
    assert coffee1 in customer.coffees()
