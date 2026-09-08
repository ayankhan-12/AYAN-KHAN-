def product(n):
    if n < 10:
        return n
    return (n % 10) * product(n // 10)

num = int(input("Enter a number: "))

print("Product of digits =", product(abs(num)))