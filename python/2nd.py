salary = float(input("Enter basic salary: "))

DA = salary * 0.10
HRA = salary * 0.20

gross_salary = salary + DA + HRA
tax = gross_salary * 0.05
net_salary = gross_salary - tax

print("DA =", DA)
print("HRA =", HRA)
print("Gross Salary =", gross_salary)
print("Tax Deduction =", tax)
print("Net Salary =", net_salary)