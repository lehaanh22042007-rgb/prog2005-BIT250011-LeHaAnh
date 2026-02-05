#bài 12
n = int(input("nhập số của bạn:"))
tong = 0
for i in range(n+1):
    if i%2 == 1:
        tong = tong + i
print(tong)
