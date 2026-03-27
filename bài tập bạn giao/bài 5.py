lst = list(map(int, input("Nhập danh sách số: ").split()))
a = []
for x in lst:
    if x % 2 == 0:
        a.append(x)
print("Danh sách số chẵn:", a)