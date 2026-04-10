#bài 3
a = []
c = 0
m = int(input("mời nhập số chữ số mà bạn muốn nhập:"))
for i in range(m):
    b = int(input())
    a.append(b)
for i in range(m):
    if a[i] % 2 == 1:
        print(a[i],"là số lẻ")
        c = c + 1
        n = a[i]
        if n >= 2:
            dem = 0
            for l in range(1, n + 1):
                if n % l == 0:
                    dem = dem + 1
            if dem == 2:
                print(n, "là số nguyên tố")
print("số lượng số lẻ:",c)