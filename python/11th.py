age = int (input("Enter age: "))
income = float (input("Enter monthly income: "))
credit_score = int (input("Enter credit score: "))

if age >= 18 and income >= 3000 and credit_score >= 650:
    print("Loan Approved!")
else:
    print("Loan Denied.")