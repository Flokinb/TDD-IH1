from sample import *

def test_single_item_no_taxes_or_shipping():
    items = [{"Name": "item1", "Price": 25, "Weight": 2, "Quantity": 1}]
    assert calculate_base_price(items) == 25

def test_multiple_items_without_taxes_and_shipping():
    items = [{"Name": "item1", "Price": 2, "Weight": 0.3, "Quantity": 2},
             {"Name": "item2", "Price": 3, "Weight": 0.1, "Quantity": 1}]
    assert calculate_base_price(items) == 7

def test_calculate_taxes():
    items = [{"Name": "item1", "Price": 1, "Weight": 0.3, "Quantity": 2},
             {"Name": "item2", "Price": 8, "Weight": 3, "Quantity": 4},
             {"Name": "item3", "Price": 3, "Weight": 2.1, "Quantity": 7}]
    location = "South Korea"
    assert calculate_taxes(items, location) == 5.5