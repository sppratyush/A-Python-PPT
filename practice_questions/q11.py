menu = {
    "pizza": 200,
    "burger": 100,
    "pasta": 150,
    "coffee": 50
}

total = 0

while True:
    print("\nMenu:", menu)
    item = input("Enter item (or 'done'): ").lower()

    if item == "done":
        break

    if item in menu:
        qty = int(input("Quantity: "))
        total += menu[item] * qty
    else:
        print("Item not available")

tax = total * 0.05
final = total + tax

print("\nTotal:", total)
print("Tax (5%):", tax)
print("Final Bill:", final)