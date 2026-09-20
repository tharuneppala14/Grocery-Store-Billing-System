print("🛒 Grocery Store Billing System")

items = {
    1: {"name": "Rice", "price": 60},
    2: {"name": "Sugar", "price": 45},
    3: {"name": "Milk", "price": 30},
    4: {"name": "Bread", "price": 40},
    5: {"name": "Eggs", "price": 70}
}

cart = []

while True:
    print("\n1. View Grocery Items")
    print("2. Add Item")
    print("3. View Cart")
    print("4. Remove Item")
    print("5. Generate Bill")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n🛍️ Grocery Items")

        for number, item in items.items():
            print(
                number,
                "-",
                item["name"],
                "- ₹",
                item["price"]
            )

    elif choice == "2":
        number = int(input("Enter item number: "))

        if number in items:
            quantity = int(input("Enter quantity: "))

            cart_item = {
                "name": items[number]["name"],
                "price": items[number]["price"],
                "quantity": quantity
            }

            cart.append(cart_item)

            print("✅ Item added to cart!")

        else:
            print("❌ Invalid item number.")

    elif choice == "3":
        if len(cart) == 0:
            print("🛒 Cart is empty.")
        else:
            print("\n🛒 Your Cart")

            for item in cart:
                total = item["price"] * item["quantity"]

                print("--------------------")
                print("Item:", item["name"])
                print("Price: ₹", item["price"])
                print("Quantity:", item["quantity"])
                print("Total: ₹", total)

    elif choice == "4":
        item_name = input("Enter item name to remove: ")

        found = False

        for item in cart:
            if item["name"].lower() == item_name.lower():
                cart.remove(item)
                print("✅ Item removed!")
                found = True
                break

        if not found:
            print("❌ Item not found.")

    elif choice == "5":
        if len(cart) == 0:
            print("🛒 Cart is empty.")
        else:
            grand_total = 0

            print("\n🧾 FINAL BILL")
            print("--------------------")

            for item in cart:
                total = item["price"] * item["quantity"]

                print(
                    item["name"],
                    "x",
                    item["quantity"],
                    "= ₹",
                    total
                )

                grand_total += total

            print("--------------------")
            print("Grand Total: ₹", grand_total)
            print("Thank you for shopping! 😊")

    elif choice == "6":
        print("Thank you for using Grocery Store Billing System! 🛒")
        break

    else:
        print("❌ Invalid choice!")
