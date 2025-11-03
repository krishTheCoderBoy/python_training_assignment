import json

class ProductSearch:
    def __init__(self, db_file=r"c:\Users\Krishnendu.Dey\Documents\python_training\polymorphism\database.json"):
        with open(db_file, "r") as f:
            self.data = json.load(f)["products"]

    def search(self, name=None, category=None, price_range=None):
        results = self.data
        if name:
            results = [p for p in results if p["name"].lower() == name.lower()]
        if category:
            results = [p for p in results if p["category"].lower() == category.lower()]
        if price_range:
            low, high = price_range
            results = [p for p in results if low <= p["price"] <= high]

        if results:
            print("\n🔎 Search Results:")
            for p in results:
                print(f"ID: {p['id']} | {p['brand']} {p['name']} | {p['category']} | Price: ₹{p['price']}")
        else:
            print("\n❌ No products found.")
        return results
