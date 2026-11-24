marks = []

for i in range(5):
    m = int(input("Enter marks: "))
    marks.append(m)

total = sum(marks)
average = total / 5
percentage = (total / 500) * 100

print("Total marks =", total)
print("Average marks =", average)
print("Percentage =", percentage, "%")