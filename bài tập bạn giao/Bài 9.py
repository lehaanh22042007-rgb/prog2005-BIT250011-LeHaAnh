s = input("Nhập câu: ")
b = s.split()
c = b[0]
for w in b:
    if len(w) > len(c):
        c = w
print("Từ dài nhất:", c)
