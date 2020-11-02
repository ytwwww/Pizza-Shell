class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_price(self):
        print(self.price)

    def __str__(self):
        return "Name: " + self.name + " Price: " + str(self.price)

    def serialize(self):
        return {"name": self.name,
                "price": self.price}


class Drink(MenuItem):
    def __init__(self, name, price):
        MenuItem.__init__(self, name, price)


class Pizza(MenuItem):
    def __init__(self, pizza_type, price):
        MenuItem.__init__(self, pizza_type, price)


# class Pizza(MenuItem):
#     def __init__(self, size, pizza_type, toppings):
#         self.price = self.calculate_price()
#         MenuItem.__init__(self, pizza_type, self.price)
#         self.size = size
#         self.toppings = toppings

#     def calculate_price(self):
#         return 'price'
