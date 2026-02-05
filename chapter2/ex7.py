#bài 7
def uoc_chung():
    a,b = int(input("nhập hai số nguyên dương của bạn:")),int(input())
    if a <=0 or b <= 0:
        print("mời nhập lại")
        uoc_chung()
    else:
        if a < b:
            for i in range(1,a+1):
                if a % i == 0 and b % i == 0:
                    c = i
                    if i > c:
                        c = i
            print(c)
        if b < a:
            for i in range(1,b+1):
                if a % i == 0 and b % i == 0:
                    c = i
                    if i > c:
                        c = i
            print(c)
uoc_chung()
