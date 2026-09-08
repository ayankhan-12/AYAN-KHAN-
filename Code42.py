marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance: "))
income = float(input("Enter family income: "))

if marks >= 80 and attendance >= 75 and income <= 300000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")