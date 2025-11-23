class Order:

    all_orders = []

    def __init__(self, customer, coffee, price):
        # Simple validation — no isinstance, no try/except
        if customer is None or coffee is None:
            print("Customer and Coffee must be provided.")
            return

        if price < 1.0 or price > 10.0:
            print("Price must be between 1.0 and 10.0")
            return

        self.customer = customer
        self.coffee = coffee
        self.price = price

        # keep track of all orders
        Order.all_orders.append(self)
