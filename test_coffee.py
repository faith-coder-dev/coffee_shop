from customer import Customer
from coffee import Coffee
from order import Order

def test_coffee_creation():
    coffee = Coffee("latte")
    assert coffee.name == "latte"

def test_coffee_orders_and_customers():
    Sheera = Customer("Sheera")
    Kendi = Customer("Kendi")
    latte = Coffee("latte")
    americano = Coffee("americano")

    order1 = Order(Sheera, latte, 5.0)
    order2 = Order(Kendi, latte, 6.0)
    order3 = Order(Sheera, americano, 7.0)

    
    assert order1 in latte.orders()
    assert order2 in latte.orders()
    assert Sheera in latte.customers()
    assert Kendi in latte.customers()

    
    assert order3 in americano.orders()
    assert Sheera in americano.customers()
