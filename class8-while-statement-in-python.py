x: int
sum: int

sum = 0
x = int(input("Enter the first number: "))

while x != 0:
    sum = sum + x
    x = int(input("Enter another number: "))

print("SUM = ", sum)

