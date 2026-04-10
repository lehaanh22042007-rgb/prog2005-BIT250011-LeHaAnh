# Bài 9
class Person:
    count = 0

    def __init__(self, name, age):
        if age <= 0:
            raise ValueError("age")
        self._name = name
        self._age = age
        Person.count += 1

    def get_name(self):
        return self._name

    def set_name(self, name):
        if name == "":
            raise ValueError("name")
        self._name = name

    def __str__(self):
        return f"{self._name} {self._age}"

    def greet(self):
        return f"Hello {self._name}"

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def is_adult(age):
        return age >= 18

    def __eq__(self, other):
        return self._age == other._age


class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        if score < 0:
            raise ValueError("score")
        self._score = score

    def get_score(self):
        return self._score

    def set_score(self, score):
        if score < 0:
            raise ValueError("score")
        self._score = score

    def __str__(self):
        return f"{self._name} {self._age} {self._score}"


p = Person("An", 20)
s = Student("Bình", 21, 8)

print(p)
print(s)
print(p.get_name())
p.set_name("Nam")
print(p)
print(p.greet())
print(Person.get_count())
print(Person.is_adult(20))
print(p == Person("C", 20))