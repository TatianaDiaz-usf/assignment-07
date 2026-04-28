# Module 7 Assignment: Organizing Data with Lists and Tuples
# TechElectronics Inventory Tracking System

# Welcome message
print("=" * 60)
print("TECHELECTRONICS INVENTORY TRACKING SYSTEM")
print("=" * 60)

# TODO 1: Create product tuples
# Each product is a tuple: (product_id, name, price, quantity, category)
# Create at least 5 product tuples
# Example: product1 = ("P001", "Smartphone X", 799.99, 10, "Mobile Phones")
product1 = ("E001", "iphone 14", 719.99 , 12, "Mobile phones")
product2 = ("E002", "ipad 11", 335, 10, "Tablet")
product3 = ("E003", "Macbook 13", 999.99 , 11, "Laptops")
product4 = ("E004", "Airpods 4", 130, 14, "Audio")
product5 = ("E005", "Roku Smart TV", 400, 13, "TV")

# TODO 2: Create an inventory list containing all product tuples
# Example: inventory = [product1, product2, ...]
inventory = [product1, product2, product3, product4, product5]

# TODO 3: Display all products
# Use a print statement to show each product in the inventory
print("\nCurrent Inventory:")
print("-" * 60)
# Add your code here to display all products
print(inventory)

# TODO 4: Access specific elements
# Use indexing to:
# - Get and display the first product (store in first_product)
# - Get and display the last product (store in last_product)
# - Get and display the third product's name only (store in third_product_name)
# - Get and display the second product's price and quantity (store in second_price, second_quantity)
first_product = inventory[0]
last_product = inventory[-1]
third_product_name = product3[1]
second_price = product2[2]
second_quantity = product2[3]

print("\n\nAccessing Specific Products:")
print("-" * 60)
# Add your code here
print(first_product)
print(last_product)
print(third_product_name)
print(second_price, second_quantity)

# TODO 5: Use slicing to get subsets
# - Get and display the first 3 products (store in first_three)
# - Get and display products from index 2 to 4 (store in middle_products)
# - Get and display all products except the first one (store in all_except_first)
first_three = inventory[0:3]
middle_products = inventory[2:4]
all_except_first = inventory[1:5]

print("\n\nProduct Subsets Using Slicing:")
print("-" * 60)
# Add your code here
print(first_three)
print(middle_products)
print(all_except_first)

# TODO 6: Add new products to inventory
# Create 2 new product tuples and add them to the inventory list
# Use the .append() method
product6 = ("E006", "Xbox", 550, 18, "Gaming")
product7 = ("E007", "Fujifilm instax", 100, 16, "Camera")
inventory.append(product6)
inventory.append(product7)

print("\n\nAdding New Products:")
print("-" * 60)
# Add your code here
print(inventory)

# TODO 7: Remove a product
# Remove the product at index 2 using .pop()
# Display what was removed and show the updated inventory
inventory.pop(2)

print("\n\nRemoving a Product:")
print("-" * 60)
# Add your code here
print(f"Removed product: {product3}")
print(f"Updated Inventory: {inventory}")

# TODO 8: Insert a product at a specific position
# Create a new product tuple and insert it at index 1
# Use the .insert() method
product8 = ("E008", "Chromebook", 450, 17, "Laptops")
inventory.insert(1, product8)

print("\n\nInserting a Product:")
print("-" * 60)
# Add your code here
print(inventory)

# REDO TODO 4 and 5: Please recalculate all access and sliced variables from todos 4 and 5, as the code grader checks these variables against the final state of the inventory.
# Add your code here
first_product = inventory[0]
last_product = inventory[-1]
third_product_name = product2[1]
second_price = product8[2]
second_quantity = product8[3]

first_three = inventory[0:3]
middle_products = inventory[2:5]
all_except_first = inventory[1:]

# TODO 9: Create category lists
# Create separate lists for different categories
# For example: mobile_phones = [], laptops = [], audio = []
# Go through your inventory and add products to appropriate category lists
audio = [product for product in inventory if product[4] == "Audio"]
tablet = [product for product in inventory if product[4] == "Tablet"]
laptops = [product for product in inventory if product[4] == "Laptops"]
tv = [product for product in inventory if product[4] == "TV"]
mobile_phones = [product for product in inventory if product[4] == "Mobile phones"]

print("\n\nProducts by Category:")
print("-" * 60)
# Add your code here
print(mobile_phones)
print(tablet)
print(audio)
print(tv)
print(laptops)

# TODO 10: Calculate inventory statistics
# Calculate and display:
# - Total number of products in inventory (store in total_products)
# - Total value of all products (price * quantity for each product) (store in total_value)
# - List of all product names (store in product_names)
# - List of all product prices (store in product_prices)
total_products = len(inventory)
total_value = sum(price[2] * price[3] for price in inventory)
product_names = [product[1] for product in inventory]
product_prices = [product[2] for product in inventory]
print("\n\nInventory Statistics:")
print("-" * 60)
# Add your code here
print(total_products)
print(f"{total_value:.2f}")
print(product_names)
print(product_prices)

# TODO 11: Find expensive products using list comprehension
# Use a list comprehension to create a list of products that cost more than $500
# Store in variable: expensive_products
# Display these expensive products
# Hint: expensive_products = [product for product in inventory if product[2] > 500]
expensive_products = [product for product in inventory if product[2] > 500]

print("\n\nExpensive Products (> $500):")
print("-" * 60)
# Add your code here
print(expensive_products)

# TODO 12: Low stock alert using list comprehension
# Use a list comprehension to create a list of products with quantity less than 5
# Store in variable: low_stock
# Display these low stock products
# Hint: low_stock = [product for product in inventory if product[3] < 5]
low_stock = [product for product in inventory if product[3] < 5]

print("\n\nLow Stock Alert (< 5 units):")
print("-" * 60)
# Add your code here
print(low_stock)

# TODO 13: Create price list using list comprehension
# Use a list comprehension to create a list of all product prices (store in original_prices)
# Then use another comprehension to apply a 10% discount to all prices (store in discounted_prices)
# Display both the original and discounted price lists
original_prices = [product[2] for product in inventory]
discount = 0.10
discounted_prices = [round(price * 0.9, 2) for price in original_prices]

print("\n\nPrice Lists:")
print("-" * 60)
# Add your code here
print(f"Original Prices: {original_prices}")
print(f"Discounted Prices: {discounted_prices}")

# TODO 14: Product name formatting using list comprehension
# Use a list comprehension to create a list of all product names in uppercase (store in uppercase_names)
# Then create another list with product codes (first 3 chars of ID + first 3 chars of name) (store in product_codes)
# Display both lists
uppercase_names = [product[1].upper() for product in inventory]
product_codes = [product[0][0:3] + product[1][0:3] for product in inventory]

print("\n\nFormatted Product Names:")
print("-" * 60)
# Add your code here
print(uppercase_names)
print(product_codes)

# TODO 15: Using Loops to Process Inventory
# Use a for loop to:
# - Count how many products are in the "Mobile Phones" category (store in mobile_count)
# - Calculate the total value of all "Laptops" in stock (store in laptop_value)
# - Find the most expensive product in the inventory (store in most_expensive)
for product in inventory:
    mobile_count = 0
    if product[4] == "Mobile phones":
        mobile_count += 1
        
for laptops in inventory:
    laptop_value = product8[2] * product8[3]

for product in inventory:
    most_expensive = max(inventory, key=lambda p: p[2])

print("\n\nLoop-Based Analysis:")
print("-" * 60)
# Add your code here
print(mobile_count)
print(laptop_value)
print(most_expensive)

# TODO 16: Using Conditionals with Lists
# Use loops and conditionals to:
# - Create a list of products that need restocking (quantity < 5) (store in restock_list)
# - Create a list of high-value items (price > $500 AND quantity > 10) (store in high_value_items)
# - Count products in different price ranges: under $100, $100-$500, over $500 (store counts in price_ranges dictionary)
for product in inventory:
    restock_list = [product for product in inventory if product[3] < 5]

for product in inventory:
    high_value_items = [product for product in inventory if product[2] > 500 and product[3] > 10 ]

under_100 = 0
between_100_500 = 0
over_500 = 0  
for product in inventory:
    if product[2] <100:
        under_100 += 1
    if product[2] >= 100 and product[2] <= 500:
        between_100_500 += 1   
    if product[2] > 500:
        over_500 += 1

price_ranges = {"under_100": under_100,
                "100_to_500": between_100_500,
                "over_500": over_500
                }
        
print("\n\nConditional Analysis:")
print("-" * 60)
# Add your code here
print(restock_list)
print(high_value_items)
print(price_ranges)

# TODO 17: Define and Use Functions
# Define these functions:
# - calculate_product_value(product): returns price * quantity for a product tuple
# - find_products_by_category(inventory, category): returns list of products in given category
# - apply_discount(inventory, discount_percent): returns new inventory with discounted prices
# Then use these functions to:
# - Calculate total inventory value
# - Find all "Audio" products
# - Create a new inventory with 15% discount applied
def calculate_product_value(product):
    return sum(price[2] * price[3] for price in inventory)

def find_products_by_category(inventory, category):
    return [product[1] for product in inventory if product[4] == "Audio"]

def apply_discount(inventory, discount_percent):
    discount_percent = 0.15
    new_prices = [prices[2] * discount_percent for prices in inventory]
    new_inventory = [inventory + new_prices]
    return new_inventory

print("\n\nFunction-Based Operations:")
print("-" * 60)
# Add your code here
print(f"Total Inventory Value: {calculate_product_value(product):.2f}")
category = [product[4] for product in inventory]
print(f"All Audio Products: {find_products_by_category(inventory,category)}")
discount_percent = 0.15
print(f"New Inventory: {apply_discount(inventory,discount_percent)}")

# TODO 18: Combine Loops, Functions, and List Operations
# Create a function generate_inventory_report(inventory) that:
# - Uses loops to analyze the inventory
# - Returns a dictionary with:
#   - 'total_products': total number of products
#   - 'total_value': sum of all (price * quantity)
#   - 'categories': list of unique categories
#   - 'low_stock': list of products with quantity < 5
#   - 'average_price': average price of all products
# Call the function and display the report
def generate_inventory_report(inventory):
    for categories in inventory:
        categories = [product[4] for product in inventory]
    for average_price in inventory:
        average_price = sum(price[2] for price in inventory)
    return {"Total Products": total_products,
            "Total Value": round(total_value, 2),
            "Categories": categories,
            "Low Stock": low_stock,
            "Average Price": average_price
            }

print("\n\nComprehensive Inventory Report:")
print("-" * 60)
# Add your code here
print(generate_inventory_report(inventory))

# TODO When calculating laptop_value, make sure to use the category name exactly "Laptops" (plural).