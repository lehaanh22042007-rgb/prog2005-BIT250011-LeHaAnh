#bài 2
import matplotlib.pyplot as plt
x = list(range(-10, 11))
y1 = [i**2 for i in x]
y2 = [i**3 for i in x]
plt.plot(x, y1, color='blue', label='y = x^2')
plt.plot(x, y2, color='red', label='y = x^3')
plt.title("Đồ thị y = x^2 và y = x^3")
plt.xlabel("Trục x")
plt.ylabel("Trục y")
plt.legend()
plt.show()