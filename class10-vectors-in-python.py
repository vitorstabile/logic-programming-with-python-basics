N: int
N = int(input("How many numbers will be enter? "))
vet: [float] = [0 for x in range(N)]

for i in range(0, N):
    vet[i] = float(input("Enter a number: "))

print()
print("TYPED NUMBERS")
for i in range(0, N):
    print(f"{vet[i]:.1f}")

