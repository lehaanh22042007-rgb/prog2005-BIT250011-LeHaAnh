#bài 6
def is_even(num):
    if num % 2 == 0:
        print("là số chẵn")
        return True

    else:
        print("là số lẻ")
        return False
b = is_even(int(input("nhập số nguyên a")))
print(b)
