lst = list(map(int, input("Nhập danh sách số (cách nhau bằng dấu cách): ").split()))
min_val = lst[0]
max_val = lst[0]
for x in lst:
    if x < min_val:
        min_val = x
    if x > max_val:
        max_val = x
print("Số nhỏ nhất:", min_val)
print("Số lớn nhất:", max_val)

