class Cart:
    def __init__(self):
        self.items = {}

    def add_items(self, **products):
        for product, qty in products.items():
            if product in self.items:
                self.items[product] += qty
            else:
                self.items[product] = qty
        print("🛒 Cart updated:", self.items)
        return self.items

    def show_cart(self):
        if not self.items:
            print("🛒 Cart is empty")
        else:
            print("\n🛒 Current Cart:")
            for item, qty in self.items.items():
                print(f"- {item} x {qty}")
