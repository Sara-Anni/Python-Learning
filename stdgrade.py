mark = int(input("Enter marks: "))


if(mark >= 90):
    print("Grade: A")
elif(mark >= 80 & mark<90):
    print("Grade: B")
elif(mark >= 70 & mark<80):
    print("Grade: C")
else:
    print("Grade: D")