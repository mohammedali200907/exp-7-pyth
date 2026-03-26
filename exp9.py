print("Mohammed Ali, 251A007")

n = int(input("Enter a number: "))
fact = 1

if n == 0:
    fact = 1
else:
    for i in range(1, n + 1):
        fact *= i

print("Factorial =", fact)
