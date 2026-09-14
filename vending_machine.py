def calculate_change(paid, price):
    change = paid - price
    return change

snack_price = 25
print("===== SNACK VENDING MACHINE =====")
print(f"This snack costs {snack_price} units.")
print("Accepted coins: 1, 5, 10, 25\n")

total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("Insert a coin (1, 5, 10, or 25): "))
    
    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid coin! Please try again.")
        continue
        
    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted: {coin} units. Running total: {total_inserted} units.\n")

    if total_inserted >= snack_price:
        print("Enough money has been inserted!")
        break

change_due = calculate_change(total_inserted, snack_price)
print("Dispensing snack... enjoy!")

if change_due == 0:
    pass
else:
    print(f"Dispensing change: {change_due} units.")

print("\n===== PURCHASE SUMMARY =====")
print(f"Snack Price:     {snack_price} units")
print(f"Coins Inserted:  {coins_inserted}")
print(f"Total Paid:      {total_inserted} units")
print(f"Change Given:    {change_due} units")
print("Thank you for using the Snack Vending Machine! Have a great day!")
