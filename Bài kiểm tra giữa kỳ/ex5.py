#bài 5
class Flower:
    def __init__(self, color):
        self.__color = color
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color
f1 = Flower("Red")
print("Màu ban đầu:", f1.get_color())
f1.set_color("Yellow")
print("Màu sau khi đổi:", f1.get_color())