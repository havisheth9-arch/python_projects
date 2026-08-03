def greet_customer(name):
  return f"Hello, {name}! Welcome to the lemonade stand!"

def calculate_total(cups, price_per_cup):
  return cups * price_per_cup

def calculate_change(total_cost, cash_paid):
  return cash_paid - total_cost

def print_receipt(name, cups, price, total, cash, change):
  print(f"\n--- Receipt for {name} ---")
  print(f"Cups of lemonade: {cups}")
  print(f"Price per cup: ${price}")
  print(f"Total cost: ${total}")
  print(f"Cash paid: ${cash}")
  print(f"Change due: ${change}")
  print(f"Thank you, {name}, for your support! Have a great day!\n")



customer_name = "Alex"
cups_ordered = 3
price_per_cup = 1.50
cash_given = 10.00

print(greet_customer(customer_name))
total_cost = calculate_total(cups_ordered, price_per_cup)
change_due = calculate_change(total_cost, cash_given)
print_receipt(
    customer_name,
    cups_ordered,
    price_per_cup,
    total_cost,
    cash_given,
    change_due,
)