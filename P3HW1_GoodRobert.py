# Robert Good
# 2024/04/28
# Assignment Name: P3HW1_Debug
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5]
# determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total_sum = sum(grades)
avg = total_sum / len(grades)

# determine letter grade for average
print("-----------------Results----------------")
print("Lowest Grade:", low)
print("Highest Grade:", high)
print("Sum of Grades:", total_sum)
print("Average:", avg)
print("------------------------------------------------")

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')
        
