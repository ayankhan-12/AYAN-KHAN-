def numbers(n):
    if n == 0:
        return

    numbers(n - 1)
    print(n, end=" ")
    print(n, end=" ")

n = int(input("Enter N: "))

numbers(n)