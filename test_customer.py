import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_creation():
    customer = Customer("Sheera")  
    assert customer.name == "Sheera"

def test_customer_orders_and_coffees():
    customer = Customer("Kendi")  
    coffee1 = Coffee("latte")     
    coffee2 = Coffee("americano") 
    order1 = Order(customer, coffee1, 6.0)  
    order2 = Order(customer, coffee2, 7.0)  
    assert order1 in customer.orders()
    assert coffee1 in customer.coffees()
