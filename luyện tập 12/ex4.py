# Bài 4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

arr = list(map(int, input().split()))
arr.append(int(input()))
k = int(input())
print(arr.count(k))

total = 0
for x in arr:
    if is_prime(x):
        total += x
print(total)

arr.sort()
print(arr)

arr.clear()
print(arr)