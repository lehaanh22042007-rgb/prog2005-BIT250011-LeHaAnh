#bài 7
numbers = list(map(int, input("Nhập các số cách nhau bằng dấu cách: ").split()))
x = int(input("Nhập số cần tìm: "))
index = -1
for i in range(len(numbers)):
    if numbers[i] == x:
        index = i
        break
if index != -1:
    print("Số", x, "nằm ở vị trí:", index)
else:
    print("Không tìm thấy số", x)
