# Main driver file to run the E-commerce Backend Simulation

from product_search import ProductSearch
from cart import Cart
from discount import Discount
from payment import CreditCardPayment, UPIPayment, CODPayment

class ECommerceSystem:
    def __init__(self):
        self.ps = ProductSearch()
        self.cart = Cart()
        self.discount_engine = Discount()

    def run(self):
        print("=== 🛍 Welcome to Mini E-Commerce System ===")

        # Step 1: Product Search
        name = input("\nEnter product name to search: ").strip()
        category = input("Enter category (or leave blank): ").strip() or None
        price_range = input("Enter price range (low,high) or leave blank: ").strip()
        if price_range:
            low, high = map(int, price_range.split(","))
            price_range = (low, high)
        else:
            price_range = None

        results = self.ps.search(name, category, price_range)
        if not results:
            return

        # Step 2: Discount Check
        choice = input("\nDo you want to check discount on a product? (yes/no): ").strip().lower()
        if choice == "yes":
            pid = int(input("Enter Product ID for discount check: "))
            product = next((p for p in results if p["id"] == pid), None)
            if product:
                self.discount_engine.get_discount(product["name"], product["price"])

        # Step 3: Cart
        while True:
            choice = input("\nDo you want to add product to cart? (yes/no): ").strip().lower()
            if choice != "yes":
                break
            pname = input("Enter product name: ").strip()
            qty = int(input("Enter quantity: "))
            self.cart.add_items(**{pname: qty})
            self.cart.show_cart()

        # Step 4: Payment
        print("\nProceeding to Payment...")
        show_payment_options()
        method = input("Choose payment method: ").strip().lower()
        total_amount = sum([10_000 * qty for qty in self.cart.items.values()])  # Dummy calc
        if method == "credit card":
            CreditCardPayment().pay(total_amount)
        elif method == "upi":
            UPIPayment().pay(total_amount)
        elif method == "cash on delivery":
            CODPayment().pay(total_amount)
        else:
            print("❌ Invalid payment method")

if __name__ == "__main__":
    system = ECommerceSystem()
    system.run()