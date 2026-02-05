#bài 3
n = int(input("mời nhập số phần tử fibonnaci bạn muốn in ra:"))
a, b = 0, 1
fibonnaci = [a, b]

for _ in range(n - 2):
    a, b = b, a + b
    fibonnaci.append(b)
print(fibonnaci)
