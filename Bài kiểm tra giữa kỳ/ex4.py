#bài 4
def tong(n):
    if n == 0:
        return 0
    return n + tong(n - 1)

n = int(input("Mời nhập số n: "))
print("Tổng =", tong(n))
