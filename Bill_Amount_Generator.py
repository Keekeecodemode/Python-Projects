print("Welcome to the Band Amount Generator")
bill = float(input("Enter the bill costed $"))
tip = int(input("Tip you would like to give 10, 12 or 15 "))
people = int(input("Enter total number of people to split: "))
amount=((bill*(tip/100))+bill)/people
print(f'Bill amount to be paid by each person = {round(amount,2)}')
