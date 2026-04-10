# Bài 6
n = int(input())
d = {}
total = 0
for _ in range(n):
    name = input()
    age = int(input())
    d[name] = age
    total += age
print(total / n)