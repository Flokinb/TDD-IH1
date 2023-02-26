from sample import *

def test_single_item_no_taxes_or_shipping():
    items = [{"Name": "item1", "Price": 25, "Weight": 2, "Quantity": 1}]
    assert calculate_base_price(items) == 25