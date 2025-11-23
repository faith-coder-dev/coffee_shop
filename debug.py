from customer import Customer
from coffee import Coffee
from order import Order


Sheera = Customer("Sheera")
Kendi = Customer("Kendi")


latte = Coffee("latte")
americano = Coffee("americano")


Order(Sheera, latte, 5.0)
Order(Kendi, latte, 6.0)
Order(Sheera, americano, 7.0)


print("Sheera's coffees:", [coffee.name for coffee in Sheera.coffees()])
print("latte customers:", [customer.name for customer in latte.customers()])
print("latte average price:", latte.average_price())
print("Most aficionado for latte:", Customer.most_aficionado(latte).name)
