# Robert Good
# 2024/05/05
# Assignment Name: P4LAB2
# counts in intervals of 5 from the two inputs user uses 
def print_incrementing_sequence(first, second):
    if second < first:
        print("Second integer can't be less than the first.")
    else:
        while first <= second:
            print(first, end=' ')
            first += 5
        print()

# Example usage:
first = int(input())
second = int(input())
print_incrementing_sequence(first, second)
