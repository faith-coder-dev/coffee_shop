from order import Order

class Coffee:
    def __init__(self, name):
        if len(name) < 3:
            print("Coffee name must be at least 3 characters.")
            return

        self.name = name

    def orders(self):
        all_orders_for_this_coffee = []
        for order in Order.all_orders:
            if order.coffee == self:
                all_orders_for_this_coffee.append(order)
        return all_orders_for_this_coffee

    def customers(self):
        customers_list = []
        for order in self.orders():
            if order.customer not in customers_list:
                customers_list.append(order.customer)
        return customers_list

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        if self.num_orders() == 0:
            return 0
        total = 0
        for order in self.orders():
            total = total + order.price
        return total / self.num_orders()
