# Bài 3
arr = list(map(int, input().split()))
s = 0
for x in arr:
    if x % 2 == 0:
        print(x, end=" ")
        s += x
print()
print(s)