# Marks Between a Range 

# Given this list:
# marks = [45, 82, 67, 91, 58, 76, 39]
# 1. Print the elements from index 2 to index 6 (excluding index 6).
# 2. Sort the list in descending order.
# 3. Print the highest and lowest marks.
marks = [45, 82, 67, 91, 58, 76, 39]
print("Elements from index 2 to 6:", marks[2:6])
marks.sort(reverse=True)
print("Sorted list in descending order:", marks)
print("Highest mark:", marks[0])
print("Lowest mark:", marks[-1])