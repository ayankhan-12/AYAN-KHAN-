num = int(input("Enter a number: "))

while num != 1 and num != 4:
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit ** 2
        num //= 10
    num = sum

if num == 1:
    print("Happy number")
else:
    print("Not a happy number")