product = ("Laptop", 50000, "Black", "Samsung", "Electronics")
print("Original Product Tuple:", product)
print("\nSecond Element of Product:", product[1])
print("\nLast Two Elements:", product[-2:])
if "Electronics" in product:
    print("\n'Electronics' is present in the product tuple.")
else:
    print("\n'Electronics' is NOT present in the product tuple.")


prices = (1000, 1500, 1200, 1100, 900)
print("\nCount of 1000 in prices:", prices.count(1000))


print("Maximum Price:", max(prices))
print("Minimum Price:", min(prices))

print("\nProduct Items:")
for item in product:
    print(f"- {item}")


product_list = list(product)
product_list[1] = 55000  # Change price
product = tuple(product_list)
print("\nUpdated Product Tuple:", product)

# 9. Add a new item using concatenation
product = product + ("In Stock",)
print("\nAfter Adding 'In Stock':", product)

# 10. Remove 'Electronics' by converting to list then back to tuple
product_list = list(product)
if "Electronics" in product_list:
    product_list.remove("Electronics")
product = tuple(product_list)
print("\nAfter Removing 'Electronics':", product)

# 11. Unpack the tuple into variables
name, price, color, brand, *rest = product
print("\nUnpacked Variables:")
print("Name:", name)
print("Price:", price)
print("Color:", color)
print("Brand:", brand)

# 12. Nested tuple with three product tuples
nested_products = (
    ("Laptop", 50000, "Samsung"),
    ("Smartphone", 20000, "Apple"),
    ("Tablet", 15000, "Lenovo")
)
print("\nName of Second Product in Nested Tuple:", nested_products[1][0])
