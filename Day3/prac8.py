# Mini Challenge: Student Result Manager Challenge

# Start with:
# names = ["Sara", "Maria", "Ayesha", "Nadia"]
# marks = [88, 54, 73, 91]
# Write a program that:
# 1. Asks the user for a student's name.
# 2. Finds that student's position in names.
# 3. Uses that position to retrieve their marks.
# 4. Prints "Pass" if the marks are at least 60; otherwise, prints "Fail".
# 5. If the name isn't found, prints "Student not found".

names = ["Sara", "Maria", "Ayesha", "Nadia"]
marks = [88, 54, 73, 91]
student_name = input("Enter the student's name: ")

if student_name in names:
    position = names.index(student_name)
    student_marks = marks[position]
    if student_marks >= 60:
        print("Pass")
    else:
        print("Fail")
else:
    print("Student not found")