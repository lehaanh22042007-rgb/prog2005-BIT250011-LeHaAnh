#bài 2
def diem_tb(d):
    tong = sum(d.values())
    so_sinh_vien = len(d)
    return tong / so_sinh_vien
students = {"Nam": 8,"Lan": 9,"Khang": 7}
dtb = diem_tb(students)
print("Điểm trung bình:", dtb)