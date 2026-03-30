#bài 3
a = 0
b = 0
while a < 30:
    a = a + 1
    if a % 2 == 1:
        b = b + a
        print(a)
print(b)