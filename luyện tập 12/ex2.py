# Bài 2
arr = [input() for _ in range(5)]
arr.sort(key=len, reverse=True)
target = input()

left = 0
right = len(arr) - 1
pos = -1

while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        pos = mid
        break
    elif len(arr[mid]) < len(target):
        right = mid - 1
    else:
        left = mid + 1

print(pos)