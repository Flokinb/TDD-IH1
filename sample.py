taxes = {
    'South Korea': 0.1,
    'China': 0.13,
    'France': 0.2
}

shipping = {
    'South Korea': 5.9,
    'China': 5.1,
    'France': 4.9
}

def calculate_total_price(items, location):
    return calculate_base_price(items) + calculate_taxes(items, location) + calculate_shipping_fees(items, location)

def calculate_base_price(items):
    total = 0
    for item in items:
        price = item["Price"]
        quantity = item["Quantity"]
        total += price * quantity
    return round(total, 2)


def calculate_taxes(items, location):
    total_taxes = 0
    for item in items:
        price = item["Price"]
        quantity = item["Quantity"]
        tax_rate = taxes[location]
        total_taxes += price * quantity * tax_rate
    return round(total_taxes, 2)

def calculate_shipping_fees(items, location):
    total_fees = 0
    for item in items:
        weight = item["Weight"]
        quantity = item["Quantity"]
        shipping_rate = shipping[location]
        total_fees += weight * quantity * shipping_rate
    return round(total_fees, 2)