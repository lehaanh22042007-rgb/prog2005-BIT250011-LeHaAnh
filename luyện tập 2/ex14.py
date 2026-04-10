# Bài 14
n = int(input())
if n < 2:
    print("Không phải số nguyên tố")
else:
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    if flag:
        print("Là số nguyên tố")
    else:
        print("Không phải số nguyên tố")