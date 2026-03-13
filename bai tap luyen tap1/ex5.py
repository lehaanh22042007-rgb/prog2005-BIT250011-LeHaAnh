#bài 5
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
A = []
B = []
print("Nhập ma trận A:")
for i in range(m):
    row = list(map(int, input().split()))
    A.append(row)
a = int(input("mời nhập cột muốn truy cập"))
b = int(input("mời nhập hàng muốn truy cập"))
for i in range(n):
    hang = A[a][i]
    B.append(hang)
print("cột",a,":")
for j in range(n):
    cot = A[b][j]
    print(cot)
print("hàng",b,":",B)
