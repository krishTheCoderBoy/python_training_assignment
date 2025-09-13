import json

class Discount:
    def __init__(self, db_file=r"c:\Users\Krishnendu.Dey\Documents\python_training\polymorphism\database.json"):
        with open(db_file, "r") as f:
            self.db = json.load(f)["discounts"]

    def get_discount(self, product_name, price):
        if product_name in self.db:
            discount = self.db[product_name]
            dtype, value = discount.get("type"), discount.get("value", 0)

            if dtype == "flat":
                final_price = max(price - value, 0)
                print(f"\n💰 Flat discount of ₹{value} on {product_name}. Final Price: ₹{final_price}")
                return final_price

            elif dtype == "percentage":
                final_price = price - (price * value / 100)
                print(f"\n💰 {value}% discount on {product_name}. Final Price: ₹{final_price}")
                return final_price

            elif dtype == "bogo":
                print(f"\n💰 Buy One Get One offer on {product_name}! Price remains ₹{price}")
                return price

        print(f"\nℹ️ No discounts available on {product_name}")
        return price
