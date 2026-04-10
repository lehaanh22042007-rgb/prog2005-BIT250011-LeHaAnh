# Bài 9
m = int(input())
n = int(input())

A = []
B = []

for i in range(m):
    row = input().split()
    if len(row) != n:
        print("Lỗi")
        exit()
    A.append(list(map(int, row)))

for i in range(m):
    row = input().split()
    if len(row) != n:
        print("Lỗi")
        exit()
    B.append(list(map(int, row)))

C = []
for i in range(m):
    r = []
    for j in range(n):
        r.append(A[i][j] + B[i][j])
    C.append(r)

for row in C:
    print(*row)