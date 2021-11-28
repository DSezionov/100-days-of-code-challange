print('Welcome to the tip colculator')
bill = float(input('What was the total bill?'))
tip = int(input('How much percent would you like to give? 10, 12 or 15?'))
people = int(input('How many people to split the bill?'))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_persons = total_bill / people

final_amount = round(bill_per_persons, 2)
final_amount = '{:.2f}'.format(bill_per_persons)
print(f'Each person should pay {final_amount}')
