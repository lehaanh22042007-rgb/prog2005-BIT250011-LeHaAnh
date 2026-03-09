#cau 1
import math

a = float(input("moi nhap he so a: "))
b = float(input("moi nhap he so b: "))
c = float(input("moi nhap he so c: "))
if a > b and a > c:
    print("so lon nhat la:",a)
    if b < c:
        print("so nho nhat la:",b)
    else:
        print("so nho nhat la:",c)
if b > a and b > c:
    print("so lon nhat la:",b)
    if a < c:
        print("so nho nhat la:",a)
    else:
        print("so nho nhat la:",c)
if c > a and c > b:
    print("so lon nhat la:",c)
    if a < c:
        print("so nho nhat la:",a)
    else:
        print("so nho nhat la:",b)
e = b ** 2 - 4 * a * c
if e > 0:
    x1 = (-b + math.sqrt(e)) / (2 * a)
    x2 = (-b - math.sqrt(e)) / (2 * a)
    print("phuong trinh co hai nghiem",x1,x2)
elif e == 0:
    print("phuong trinh co vo so nghiem")
else:
    print("phuong trinh vo nghiem")
