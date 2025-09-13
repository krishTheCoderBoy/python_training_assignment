# create a product tuple
product = ("Laptop", 50000, "Black", "Samsung", "Electronics")
print("Product tuple:", product)

# print the second element
print("Second element:", product[1])

# slice the last two elements
print("Last two elements:", product[-2:])

# check if "Electronics" is present
if "Electronics" in product:
    print("Electronics is present")
else:
    print("Electronics is not present")

# tuple of prices
prices = (1000, 1500, 1200, 1100, 900)
print("Count of 1000:", prices.count(1000))

# max and min price
print("Max price:", max(prices))
print("Min price:", min(prices))

# print each item in product
print("Product details:")
for item in product:
    print(item)

# convert tuple to list, change price, back to tuple
product_list = list(product)
product_list[1] = 55000
product = tuple(product_list)
print("Updated product tuple:", product)

# add new item using concatenation
product = product + ("In Stock",)
print("After adding new item:", product)

# remove 'Electronics'
product_list = list(product)
if "Electronics" in product_list:
    product_list.remove("Electronics")
product = tuple(product_list)
print("After removing Electronics:", product)

# unpack tuple into variables
name = product[0]
price = product[1]
color = product[2]
brand = product[3]
print("Name:", name)
print("Price:", price)
print("Color:", color)
print("Brand:", brand)

# nested tuple
nested_products = (
    ("Laptop", 50000, "Samsung"),
    ("Smartphone", 20000, "Apple"),
    ("Tablet", 15000, "Lenovo")
)

# access name of second product
print("Second product name:", nested_products[1][0])
