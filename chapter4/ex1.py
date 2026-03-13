#bài 1
def tinh_toan(t):
    total = sum(t)
    max_value = max(t)
    min_value = min(t)
    return total, max_value, min_value
numbers = (3, 7, 2, 9, 5)
tong, lon_nhat, nho_nhat = tinh_toan(numbers)
print("Tổng:", tong)
print("Giá trị lớn nhất:", lon_nhat)
print("Giá trị nhỏ nhất:", nho_nhat)