import json

class Payment:
    def pay(self, amount):
        print(f"Paying ₹{amount} using generic method")

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"✅ Paid ₹{amount} using Credit Card")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"✅ Paid ₹{amount} using UPI")

class CODPayment(Payment):
    def pay(self, amount):
        print(f"✅ Paid ₹{amount} as Cash on Delivery")

def show_payment_options(db_file="database.json"):
    with open(db_file, "r") as f:
        methods = json.load(f)["payment_methods"]
    print("\n💳 Available Payment Methods:")
    for mode in methods:
        print(f"- {mode}")
    return methods
