#bài 4
class Hoa:
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau
    def __str__(self):
        return f"Tên hoa: {self.ten}, Màu: {self.mau}"
hoa1 = Hoa("Hoa hồng", "Đỏ")
print(hoa1)