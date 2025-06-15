# cart.py
class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, qty, price):
        if item in self.items:
            self.items[item]['qty'] += qty
        else:
            self.items[item] = {'qty': qty, 'price': price}

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def calculate_total(self):
        return sum(v['qty'] * v['price'] for v in self.items.values())

    def show_cart(self):
        if not self.items:
            print("Cart is empty.")
            return
        print("\nYour Cart:")
        for item, data in self.items.items():
            print(f"{item.capitalize()} x{data['qty']} @ ₹{data['price']} = ₹{data['qty'] * data['price']}")
