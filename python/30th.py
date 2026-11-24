n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    m = float(input("Enter marks: "))
    marks.append(m)

total = sum(marks)
average = total / n

highest = max(marks)
lowest = min(marks)

passed = 0
failed = 0
above_75 = 0

for m in marks:
    if m >= 40:
        passed = passed + 1
    else:
        failed = failed + 1

    if m > 75:
        above_75 = above_75 + 1

print("Class Average =", average)
print("Highest Marks =", highest)
print("Lowest Marks =", lowest)
print("Passed Students =", passed)
print("Failed Students =", failed)
print("Students scoring above 75% =", above_75)