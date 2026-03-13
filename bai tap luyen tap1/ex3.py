#bài 3
def cuu_chuong():
    a = int(input("Mời nhập số trong khoảng 1-9:"))
    if a <= 9 and a >= 1:
        for i in range(1,10):
            print(a,"x",i,"=",a*i)
    else:
        a = int(input("Mời nhập số trong khoảng 1-9:"))
        cuu_chuong()
cuu_chuong()
