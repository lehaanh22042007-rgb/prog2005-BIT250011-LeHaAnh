#bài 1
def cuu_chuong():
    a = int(input("mời nhập một số từ 1 đến 9"))
    if a > 0 and a <= 9:
        for b in range(1, 10):
            print(a,"x",b,"=",a*b)
    else:
        print("mời nhập lại")
        cuu_chuong()
cuu_chuong()
