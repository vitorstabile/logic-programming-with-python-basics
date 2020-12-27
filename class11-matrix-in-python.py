M: int
N: int

M = int(input("How many rows the matrix will be? "))
N = int(input("How many columns the matrix will be? "))

mat: [[int]] = [[0 for x in range(N)] for x in range(M)]

for i in range(0, M):
    for j in range(0, N):
        mat[i][j] = int(input(f"Element [{i},{j}]: "))

print()
print("Typed Matrix:")
for i in range(0, M):
    for j in range(0, N):
        print(f"{mat[i][j]} ", end="")
    print()
