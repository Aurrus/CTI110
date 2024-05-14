# Robert Good
# 2024/04/21
# Assignment Name: P1HW2
# Brief description of program:Budget for trips

#User inputs for destination,budget,gas, accommodation, and food expenses
print("This Program calculates and displays travel expenses", "\n")
budget = float(input("Enter Budget: "))
print()

destination = input("Enter your travel destination: ")
print()

gas_expense = float(input("How much do you think you will spend on gas? "))
print()

accommodation_expense = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()

food_expense = float(input("Last, how much do you need for food? "))
print()
# calculations
total_expenses = gas_expense + accommodation_expense + food_expense
remaining_budget = budget - total_expenses

print("----------Travel Expenses----------")
print("Location:          ",destination)
print("Initial Budget:    ",f'${budget:.2f}')
print(f"Fuel:              ",f'${gas_expense:.2f}')
print(f"Accomodation:      ",f'${accommodation_expense:.2f}')
print(f"Food:              ",f'${food_expense:.2f}')
print("-----------------------------------")

print("Remaining Balance: ",f'${remaining_budget:.2f}')
