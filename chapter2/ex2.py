def nguyen_to(n):
    if n < 2:
        return (n, "không phải số nguyên tố")
    for i in range(2, n):
        if n % i == 0:
            return (n, "không phải số nguyên tố")
    return (n, "là số nguyên tố")

def sd_nguyen_to():
    n = int(input("mời nhập số nguyên dương: "))
    if n <= 0:
        print("số trên không phải số dương. Mời nhập lại")
        sd_nguyen_to()
    else:
        print(nguyen_to(n))

sd_nguyen_to()
