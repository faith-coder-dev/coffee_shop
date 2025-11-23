from customer import Customer
from coffee import Coffee
from order import Order

# Create Customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create Coffees
espresso = Coffee("Espresso")
cappuccino = Coffee("Cappuccino")

# Create Orders
Order(alice, espresso, 5.0)
Order(bob, espresso, 6.0)
Order(alice, cappuccino, 7.0)

# Test outputs
print("Alice's coffees:", [coffee.name for coffee in alice.coffees()])
print("Espresso customers:", [customer.name for customer in espresso.customers()])
print("Espresso average price:", espresso.average_price())
print("Most aficionado for Espresso:", Customer.most_aficionado(espresso).name)
