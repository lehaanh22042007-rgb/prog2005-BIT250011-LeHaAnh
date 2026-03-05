#bài 11
numbers = list(map(int, input("Nhập các số cách nhau bằng dấu cách: ").split()))
max = numbers[0]
min = numbers[0]
for num in numbers:
    if num > max:
        max = num
    if num < min:
        min = num
print("Giá trị lớn nhất:", max)
print("Giá trị nhỏ nhất:", min)
