count = 0
sum = 0

while True:
    num = float(input("Enter number (-1 to stop): "))

    if num == -1:
        break

    sum += num
    count += 1

print("Count =", count)

if count > 0:
    print("Average =", sum / count)
else:
    print("No numbers entered")