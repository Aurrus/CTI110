# Robert Good
# 2024/05/10
# Assignment Name: P5LAB
# This program gives you amount of change owed from the amount you put in the registered


import random
#math
def disperse_change(change):
    dollars = change // 1
    change %= 1
    quarters = change // 0.25
    change %= 0.25
    dimes = change // 0.10
    change %= 0.10
    nickels = change // 0.05
    change %= 0.05
    pennies = round(change / 0.01)
#change amount in respective value
    print("")
    if dollars > 0:
        print("Dollars:", int(dollars))
    if quarters > 0:
        print("Quarters:", int(quarters))
    if dimes > 0:
        print("Dimes:", int(dimes))
    if nickels > 0:
        print("Nickels:", int(nickels))
    if pennies > 0:
        print("Pennies:", int(pennies))
#statements asking for value for register and what it displays in response
def main():
    amount_owed = round(random.uniform(0.01, 100.00),2)
    print("You owe:", amount_owed)
    cash_paid = float(input("How much cash will you put in the self-checkout? "))
    change_due = cash_paid - amount_owed
    print(f"Change is: {change_due:.2f} ")
    disperse_change(change_due)

if __name__ == "__main__":
    main()
    
