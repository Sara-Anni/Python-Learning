# Tuple Statistics Medium

# Given this tuple:
# numbers = (4, 7, 4, 2, 9, 4, 7, 1)
# 1. Count how many times 4 appears.
# 2. Find the index of the first 7.
# 3. Create and print a new tuple containing only the elements from index 2 to index 6 (excluding index 6).

numbers = (4, 7, 4, 2, 9, 4, 7, 1)
count_of_4 = numbers.count(4)
index_of_first_7 = numbers.index(7)
new_tuple = numbers[2:6]   
print("Count of 4:", count_of_4)
print("Index of first 7:", index_of_first_7)
print("New tuple from index 2 to 6:", new_tuple)
