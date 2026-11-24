math = float(input("Enter mathematics marks (out of 100): "))
physics = float(input("Enter physics marks (out of 100): "))
chemistry = float(input("Enter chemistry marks (out of 100): "))

overall_pct = (math + physics + chemistry) / 3

if math >= 60 and physics >= 55 and chemistry >=50 and overall_pct >= 60:
    print("Result: Eligible for admission.")
else:
    print("Result: Not eligible for admission.")