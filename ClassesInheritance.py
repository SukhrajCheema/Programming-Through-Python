class Customer:
    """defines a customer that can place order at a cafe."""

    def __init__(self, name, loyalty_discount):
        self.name = name
        self.loyalty_discount = loyalty_discount


class Order:
    """a schedule of items ordered and the cost for a particular customer."""

    def __init__(self, customer):
        self.customer = customer
        self.cost = 0.0
        self.itemsOrdered = []

    def addToOrder(self, item):
        self.itemsOrdered.append(item)
        self.cost += item.price

    def summariseOrder(self):
        print(f"Customer: {self.customer.name}")
        print(f"Total items ordered: {len(self.itemsOrdered)}")
        for x in self.itemsOrdered:
            x.displayDetails()
        # Apply discounts
        if self.customer.loyalty_discount:
            savings = 0.0
            for x in self.itemsOrdered:
                savings += x.discount
            self.cost -= savings
            print(f'Today you saved £{savings:.2f}')
        print(f'Total cost: £{self.cost:.2f}')


class Item:
    """super class for all food and drink that can be ordered at the cafe."""

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Drink(Item):
    """sub class of item and serves as super class for all drink items we can purchase."""

    def __init__(self, name, price, size):  # include all attributes of parent and child classes. Old = new attributes.
        super().__init__(name, price)  # second init call does not need 'self' attribute. Only old attributes.
        self.size = size
        self.discount = 0.10


class Tea(Drink):
    """sub class of drink to represent a cup of tea that we can order."""

    def __init__(self, name, price, size, flavor):
        super().__init__(name, price, size)
        self.flavor = flavor

    def displayDetails(self):
        print(f"{self.name}, {self.price}, {self.flavor}")


class MineralWater(Drink):
    """sub class of drink to represent water we can order."""

    def __init__(self, name, price, size, isCarbonated):
        super().__init__(name, price, size)
        self.isCarbonated = isCarbonated

    def displayDetails(self):
        if self.isCarbonated:
            print(f"{self.name}, carbonated.")
        else:
            print(f"{self.name}.")


class Cake(Item):
    """subclass of item, represents a fucking cake obvs."""
    def __init__(self, name, price, sliceSize, type, hasNuts):
        super().__init__(name, price)
        self.sliceSize = sliceSize
        self.type = type
        self.hasNuts = hasNuts
        self.discount = 0.0

    def displayDetails(self):
        if self.hasNuts:
            print(f"{self.name} {self.price}, {self.sliceSize}, {self.type}")
        else:
            print(f"{self.name} {self.price}, {self.sliceSize}, {self.type}")
            print("Warning: contains nuts!")


class Sandwich(Item):
    """subclass of item, a sandwich"""
    def __init__(self, name, price, breadType, filling):
        super().__init__(name, price)
        self.breadType = breadType
        self.filling = filling
        self.discount = 0.20

    def displayDetails(self):
        print(f"{self.name} {self.price}, {self.breadType}, {self.filling}")


def main():
    # Create two customers ...
    cust1 = Customer('Harry Palmer', False)
    cust2 = Customer('Bill Preston', True)  # A loyal regular customer

    # Order some items ...
    order1 = Order(cust1)
    order1.addToOrder(Tea('Black tea', 2.00, 'large','Earl Gray'))
    order1.addToOrder(Sandwich('Club special',4.50,'brown','chicken'))

    order2 = Order(cust2)
    order2.addToOrder(MineralWater('Evian',1.50,'small',False))
    order2.addToOrder(Sandwich('Simple sandwich',1.50,'white','cheese'))
    order2.addToOrder(Cake('Chocolate dream',2.30,'medium','chocolate',True))

    # Summarise our orders ...
    order1.summariseOrder()
    print()
    order2.summariseOrder()
    print()


if __name__ == "__main__":
    main()


