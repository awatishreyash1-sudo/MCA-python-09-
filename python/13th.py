correct_pin = "1234"
balance = 5000.0

pin = input("Enter your PIN: ")
if pin != correct_pin:
    print("Error: Incorrect PIN.")
else:
    print(f"PIN correct. Your balance is ${balance}")

    amount = float(input("Enter amount to withdraw: "))

    if amount <=0: 
        float(input("Enter amount."))
    elif amount > balance:
        print("Error: Insufficient fonds.")
    else:
        balance -= amount
        print(f"Success! dispensing ${amount}")
        print(f"Remaining balance: ${balance}")