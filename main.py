from pyscript import display
# Restaurant Order System using Python Data Types

# String data type
restaurant_name = "DK Caffè"
owner_name = "Daniella Catam"

# Integer data type
year_since = 2025

# Float data type
tax_rate = 0.08  # 8% tax

# Boolean data type
has_delivery = True
is_dine_in = True
is_takeaway = False

# List data type
product_names = ["Strawberry Matcha", "Croissant with Nutella", "Pomegrante Black Tea"]
extra = ["Cheese Roll", "Bottled Water"]

# Tuple data type
business_hours = ("11:00 AM", "10:00 PM")

# Dictionary data type
menu = {
    "Strawberry Matcha": 125.00,
    "Pomegranate Black Tea": 140.00,
    "Croissant with Nutella": 100.00,
    "Cheese Roll": 30.00,
    "Bottled Water": 20.00
}

# Set data type
common_allergens = {"gluten", "dairy", "nuts"}

# Displaying restaurant information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display(f"Menu Pricelist", target="heading1")

# Display menu items
display(product_names[0], target="prod1")
display(f"₱{menu['Strawberry Matcha']:.2f}", target="price1")
display(product_names[1], target="prod2")
display(f"₱{menu['Croissant with Nutella']:.2f}", target="price2")
display(product_names[2], target="prod3")
display(f"₱{menu['Pomegranate Black Tea']:.2f}", target="price3")
display(extra[0], target="prod4")
display(f"₱{menu['Cheese Roll']:.2f}", target="price4")
display(extra[1], target="prod5")
display(f"₱{menu['Bottled Water']:.2f}", target="price5")

# Display additional information
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")


# Display order type
display(f"Dine-in & Takeout Available", target="orderType")