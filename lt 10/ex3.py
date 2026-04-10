#bài 3
a = int(input("mời nhập số mà bạn muốn tìm giai thừa:"))
def product(i,b):
    if i > 1:
        return product(i-1,b*i)
    else:
        print(b)
product(a,1)

