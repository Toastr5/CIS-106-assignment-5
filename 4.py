start = str(input('Do you want to use this program (y/n)? '))
total_employees = 0 
while start == 'n':
  start = str(input('Do you want to use this program (y/n)? '))
while start == 'y':
  name = str(input('Enter your name: '))
  hours = float(input('Enter hours worked: '))
  pay_rate = float(input('Enter pay rate: '))
  if hours > 40:
    overtime = hours - 40
    overtime_pay = overtime * (pay_rate * 1.5)
    gross_pay = (40 * pay_rate) + overtime_pay
    print(f"{name} \nGross pay: ${gross_pay} \nOvertime:{overtime} hr")
  else:
    gross_pay = hours * pay_rate
    print(f"{name} \nGross pay: ${gross_pay}")
  total_employees = total_employees + 1
  print(f"total employees: {total_employees}")
  start = str(input('Do you want to use this program (y/n)? '))
