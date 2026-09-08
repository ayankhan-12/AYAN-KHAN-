hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))

hour = hour % 12
angle = abs((hour * 30 + minute * 0.5) - (minute * 6))

if angle > 180:
    angle = 360 - angle

print("Smaller angle =", angle)