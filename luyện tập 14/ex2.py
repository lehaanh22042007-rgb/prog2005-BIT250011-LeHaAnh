#bài 2
a = []
for i in range(5):
    b = str(input("mời nhập tên người tiếp theo:"))
    a.append(b)
print(a)
a.pop(1)
print("danh sách sau khi xóa tên người thứ 2:",a)
