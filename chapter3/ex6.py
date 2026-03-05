#bài 6
numbers = list(map(int, input("Nhập các số nguyên cách nhau bằng dấu cách: ").split()))
b = 0
n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            b += 1
print("Danh sách sau khi sắp xếp:", numbers)
print("Số lần hoán đổi:", b)
