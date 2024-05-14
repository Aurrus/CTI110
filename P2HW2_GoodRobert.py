# Robert Good
# 2024/04/21
# Assignment Name: Grade Analysis Program
# Brief description of program: This asks users for Grades for 6 modules and calculates data(average, highest, lowest, sum of grades) 


def calculate_average(grades):
    return sum(grades) / len(grades)
#storage
grades_list = []

# User inputs for grades
for i in range(1, 7):
    grade = float(input(f"Enter grade for Module {i}: "))
    grades_list.append(grade)

# Calculations
lowest_grade = min(grades_list)
highest_grade = max(grades_list)
sum_of_grades = sum(grades_list)
average_grade = calculate_average(grades_list)

# Displays calculations
print("------------Results------------")
print("Lowest grade:", lowest_grade)
print("Highest grade:", highest_grade)
print("Sum of grades:", sum_of_grades)
print("Average grade:", "{:.2f}".format(average_grade))
print("---------------------------------------")
