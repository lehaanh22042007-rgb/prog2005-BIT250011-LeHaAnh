# Bài 9
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("...")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Gâu gâu")

d = Dog("Milo")
d.sound()