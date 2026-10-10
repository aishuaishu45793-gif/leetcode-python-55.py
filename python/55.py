# 127. Check Armstrong Number

number = 153
digits = str(number)
power = len(digits)

total = 0

for digit in digits:
    total += int(digit) ** power

if total == number:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")