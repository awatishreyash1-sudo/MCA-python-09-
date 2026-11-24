start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

count = 0

print("Prime numbers:")

for num in range(start, end + 1):
    prime = True

    if num < 2:
        prime = False

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)
        count = count + 1

print("Total prime numbers =", count)