x: int
sum: int

N = int(input("How many number will be enter? "))

sum = 0
for i in range(0, N):
    x = int(input("Enter a number: "))
    sum = sum + x

print("SUM = ", sum)

