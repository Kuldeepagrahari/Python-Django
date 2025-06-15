from store import get_price, list_items
from cart import Cart
import json, os
from datetime import datetime

cart = Cart()

def load_discounts():
    try:
        with open("discounts.json") as f:
            return json.load(f)
    except Exception as e:
        print("Error loading discount codes:", e)
        return {}

def apply_discount(total, code, discounts):
    if code in discounts:
        discount_percent = discounts[code]
        discount_amount = total * (discount_percent / 100)
        return total - discount_amount, discount_amount
    return total, 0

def save_bill(cart, total, discount_amt):
    os.makedirs("data", exist_ok=True)
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/bill_{now}.txt"
    with open(filename, "w") as f:
        for item, data in cart.items.items():
            f.write(f"{item}: {data['qty']} x ₹{data['price']} = ₹{data['qty']*data['price']}\n")
        f.write(f"\nDiscount: ₹{discount_amt}\n")
        f.write(f"Total Payable: ₹{total}\n")
    print(f"Bill saved as {filename}")

def main():
    print("🛒 Welcome to Python Grocery Store 🛒")
    discounts = load_discounts()
    while True:
        print("\n1. View Items\n2. Add to Cart\n3. View Cart\n4. Checkout\n5. Exit")
        choice = input("Choose an option: ")

        try:
            if choice == '1':
                list_items()

            elif choice == '2':
                item = input("Enter item name: ").lower()
                price = get_price(item)
                if price is None:
                    print("Item not found.")
                    continue
                qty = int(input("Enter quantity: "))
                cart.add_item(item, qty, price)
                print("Added to cart.")

            elif choice == '3':
                cart.show_cart()

            elif choice == '4':
                total = cart.calculate_total()
                cart.show_cart()
                print(f"\nSubtotal: ₹{total}")
                code = input("Enter discount code (if any): ").strip().upper()
                total_after_discount, discount_amt = apply_discount(total, code, discounts)
                print(f"Discount Applied: ₹{discount_amt}")
                print(f"Total Payable: ₹{total_after_discount}")
                save_bill(cart, total_after_discount, discount_amt)
                break

            elif choice == '5':
                print("Thanks for visiting!")
                break

            else:
                print("Invalid choice.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
