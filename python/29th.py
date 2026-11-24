while True:

    print("\n1. Prime")
    print("2. Palindrome")
    print("3. Armstrong")
    print("4. Factorial")
    print("5. Fibonacci Series")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter number: "))
        count = 0

        for i in range(1, num + 1):
            if num % i == 0:
                count = count + 1

        if count == 2:
            print("Prime number")
        else:
            print("Not a prime number")

    elif choice == 2:
        num = int(input("Enter number: "))
        original = num
        reverse = 0

        while num > 0:
            digit = num % 10
            reverse = reverse * 10 + digit
            num = num // 10

        if original == reverse:
            print("Palindrome number")
        else:
            print("Not a palindrome number")

    elif choice == 3:
        num = int(input("Enter number: "))
        original = num
        total = 0

        while num > 0:
            digit = num % 10
            total = total + digit ** 3
            num = num // 10

        if total == original:
            print("Armstrong number")
        else:
            print("Not an Armstrong number")

    elif choice == 4:
        num = int(input("Enter number: "))
        fact = 1

        for i in range(1, num + 1):
            fact = fact * i

        print("Factorial =", fact)

    elif choice == 5:
        n = int(input("Enter number of terms: "))

        a = 0
        b = 1

        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b

        print()

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid choice")