#bài 4
import matplotlib.pyplot as plt
cities = ["Los Angeles", "San Diego", "San Jose", "San Francisco","Fresno", "Sacramento", "Long Beach", "Oakland","Bakersfield", "Anaheim"]
area = [1302, 964, 469, 121, 300, 259, 132, 202, 388, 131]
data = list(zip(cities, area))
data.sort(key=lambda x: x[1], reverse=True)
cities_sorted = [x[0] for x in data]
area_sorted = [x[1] for x in data]
plt.barh(cities_sorted, area_sorted)
plt.gca().invert_yaxis()
plt.title("Top 10 thành phố California theo diện tích")
plt.xlabel("Diện tích (km²)")
plt.ylabel("Thành phố")
plt.show()