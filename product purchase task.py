# Catalog section with product prices
catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}


# Discount rules section
discount_rules = {
    "flat_10_discount": {"type": "flat", "amount": 10, "condition": lambda total: total > 200},
    "bulk_5_discount": {"type": "percentage", "amount": 5, "condition": lambda quantity: quantity > 10},
    "bulk_10_discount": {"type": "percentage", "amount": 10, "condition": lambda quantity: quantity > 20},
    "tiered_50_discount": {"type": "percentage", "amount": 50, "condition": lambda quantity: quantity > 30}
}


# Fee section
gift_wrap_fee = 1
shipping_fee_per_package = 5
products_per_package = 10


# calculations section
def product_total_func(product, quantity, gift_wrapped):
    price = catalog[product]
    total = price * quantity
    if gift_wrapped:
        total += gift_wrap_fee * quantity
    return total



def discount_func(subtotal, quantity):
    applicable_discounts = {}
    for discount_name, discount_rule in discount_rules.items():
        if discount_rule["condition"](quantity):
            if discount_rule["type"] == "flat":
                discount_amount = discount_rule["amount"]
            elif discount_rule["type"] == "percentage":
                discount_amount = subtotal * discount_rule["amount"] / 100
            applicable_discounts[discount_name] = discount_amount
    if applicable_discounts:
        return max(applicable_discounts.values())
    return 0



def shipping_fee_func(quantity):
    return (quantity // products_per_package) * shipping_fee_per_package



# Getting user inputs
product_quantities = {}
product_gift_wraps = {}
for product in catalog:
    quantity = int(input(f"Enter the quantity of {product}: "))
    gift_wrapped = input(f"Is {product} wrapped as a gift? (yes/no): ").lower() == "yes"
    product_quantities[product] = quantity
    product_gift_wraps[product] = gift_wrapped



# subtotal section
subtotal = 0
for product, quantity in product_quantities.items():
    total = product_total_func(product, quantity, product_gift_wraps[product])
    subtotal += total
    print(f"{product}: Quantity: {quantity}, Total: ${total}")



# discount section
discount = discount_func(subtotal, sum(product_quantities.values()))



# shipping fee section
shipping_fee = shipping_fee_func(sum(product_quantities.values()))



# total amount
total = subtotal - discount + shipping_fee



# results
print("Subtotal: $" + str(subtotal))
if discount > 0:
    print("Discount Applied: $" + str(discount))
print("Shipping Fee: $" + str(shipping_fee))
print("Total: $" + str(total))
