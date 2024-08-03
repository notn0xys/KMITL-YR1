name = input("Enter Employee's name: ")
no_of_hours = float(input("Enter The amount of hours worked in a week: "))
pay_rate = float(input("Enter Hourly Payrate: "))
tax_withholding_rate = float(input("Enter federal tax withholding rate: "))
state_tax_withholding = float(input("Enter State tax withholding rate: "))

grosspay = no_of_hours * pay_rate
fed_taxed = grosspay * tax_withholding_rate
display_fed = tax_withholding_rate * 100
display_state = state_tax_withholding * 100
state_taxed = grosspay * state_tax_withholding
total_taxxed = fed_taxed + state_taxed
net_pay = grosspay - total_taxxed

print("Employee's Name: " + name)
print(f"Hours worked: {no_of_hours}")
print(f"Pay Rate: ${pay_rate}" )
print(f"Gross Pay: ${grosspay:.2f}" )
print("Deductions:")
print(f" Federal Withholding ({display_fed:.1f}%) : ${fed_taxed:.2f}")
print(f" State Withholding ({display_state:.1f}%) : ${state_taxed:.2f}")
print(f" Total Deduction : ${total_taxxed:.2f}")
print(f"Net Pay : ${net_pay:.2f}")




