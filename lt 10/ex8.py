#bài8
a1 = str(input("chuỗi 1:"))
a2 = str(input("chuỗi 2:"))
a3 = str(input("chuỗi 3:"))
a4 = str(input("chuỗi 4:"))
a5 = str(input("chuỗi 5:"))
a =[len(a1),len(a2),len(a3),len(a4),len(a5)]
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                print(lst)
bubble_sort(a)
print(a)