a = int(input("mời nhập số nguyên dương a:"))
b = int(input("mời nhập số nguyên dương b:"))
c = []
if a > b:
    for i in range (1,b+1):
        if a % i ==0 and b % i ==0:
            c.append(i)
            c.sort()
if b > a:
    for i in range (1,a+1):
        if b % i ==0 and a % i ==0:
            c.append(i)
            c.sort()
print(c)
