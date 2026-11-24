data = float(input("Enter monthly data usage in GB: "))

if data <= 5:
    bill = data * 10
elif data <= 10:
    bill = (5 * 10) + ((data - 5) * 8)
else:
    bill = (5 * 10) + (5 * 8) + ((data - 10) * 5)

print("Total Mobile Data Bill =", bill)