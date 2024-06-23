start = str(input("Do you want to start the program? (y/n): "))
total_discount = 0
while start == "n":
  start = str(input("Do you want to start the program? (y/n): "))

while start == "y":
  quantity = int(input("Enter quantity: "))
  unit_price = float(input("Enter unit price: "))
  extended_price = quantity * unit_price
  if extended_price > 10000.00:
    discount = extended_price * 0.25
    print(f"Extended price: ${extended_price} \nDiscount: 25%         \nDiscounted Price: ${extended_price - discount}")
  else:
    discount = extended_price * 0.10
    print(f"Extended price: ${extended_price} \nDiscount: 10%         \nDiscounted Price: ${extended_price - discount}")
  total_discount = total_discount + discount
  start = str(input("Do you want to start the program? (y/n): "))
print(f"Total Discount: ${total_discount}")