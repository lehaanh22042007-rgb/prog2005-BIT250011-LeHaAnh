#bài 3
students = {"Nam": 8,"Lan": 9,"Khang": 7}
key = input("Nhập tên sinh viên cần kiểm tra: ")
if key in students:
    print("Key tồn tại trong dictionary")
else:
    print("Key không tồn tại trong dictionary")