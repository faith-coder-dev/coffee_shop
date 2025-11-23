from order import Order

class Customer:
    def __init__(self, name):
        if len(name) < 1 or len(name) > 15:
            print("Customer name must be between 1 and 15 characters.")
            return

        self.name = name

    def orders(self):
        customer_orders = []
        for order in Order.all_orders:
            if order.customer == self:
                customer_orders.append(order)
        return customer_orders

    def coffees(self):
        coffee_list = []
        for order in self.orders():
            if order.coffee not in coffee_list:
                coffee_list.append(order.coffee)
        return coffee_list

    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order

    @classmethod
    def most_aficionado(cls, coffee):
        top_customer_name = None
        top_amount = 0

       
        for order in Order.all_orders:
            if order.coffee == coffee:
                amount = order.price
                if amount > top_amount:
                    top_amount = amount
                    top_customer_name = order.customer.name

        if top_customer_name != None:
            for order in Order.all_orders:
                if order.customer.name == top_customer_name:
                    return order.customer

        return None
