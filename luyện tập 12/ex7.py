# Bài 7
name = input()
age = input()
id = input()

with open("nhanvien.txt", "w") as f:
    f.write(f"{name},{age},{id}")

import csv
with open("nhanvien.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "id"])
    writer.writerow([name, age, id])

with open("nhanvien.txt", "r") as f:
    print(f.read())

with open("nhanvien.csv", "r") as f:
    print(f.read())