class Product():
    def __init__(self, id, name, price, qty):
        self.id = id
        self.name = name
        self.price = price
        self.qty = qty

    def display_product(self):
        print(f"Product id : {self.id}")
        print(f"Product Name : {self.name}")
        print(f"Product id : {self.price}")
        print(f"Product id : {self.qty}")