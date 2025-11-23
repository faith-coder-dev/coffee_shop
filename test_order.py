from customer import Customer
from coffee import Coffee
from order import Order



def test_order_creation():
    customer = Customer("Sheera")
    coffee = Coffee("Iatte")
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0
