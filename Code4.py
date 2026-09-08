choice = input("Enter C to convert Celsius to Fahrenheit or F to convert Fahrenheit to Celsius: ")

if choice == "C" or choice == "c":
    C = float(input("Enter temperature in Celsius: "))
    F = (C * 9 / 5) + 32
    print("Temperature in Fahrenheit:", F)

elif choice == "F" or choice == "f":
    F = float(input("Enter temperature in Fahrenheit: "))
    C = (F - 32) * 5 / 9
    print("Temperature in Celsius:", C)

else:
    print("Invalid choice")
