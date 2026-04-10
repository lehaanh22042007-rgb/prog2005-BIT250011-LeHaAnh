# Bài 11
class SinhVien:
    count = 0

    def __init__(self, diem):
        self.diem = diem
        SinhVien.count += 1

    @classmethod
    def dem(cls):
        return cls.count

sv1 = SinhVien(7)
sv2 = SinhVien(8)
print(SinhVien.dem())