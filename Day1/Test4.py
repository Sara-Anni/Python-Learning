#4. Convert Minutes
minutes = int(input("Enter the number of minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(minutes, "minutes is equal to", hours, "hours and", remaining_minutes, "minutes.")