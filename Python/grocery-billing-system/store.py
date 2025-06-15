
INVENTORY = {
    "apple": 30,
    "banana": 10,
    "bread": 25,
    "milk": 50,
    "rice": 40
}
itemsCnt = len(INVENTORY)
def get_price(item):
    return INVENTORY[item.lower()]

def list_items():
    print("Available Items:")
    for item, price in INVENTORY.items():
        print(item, ": ₹", price)

# print(get_price("Apple"))
list_items()