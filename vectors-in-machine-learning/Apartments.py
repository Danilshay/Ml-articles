import matplotlib.pyplot as plt

apartments = {
    "Apartment A": (35, 5),
    "Apartment B": (50, 3),
    "Apartment 1": (45, 1.0),
    "Apartment 2": (47, 1.2),
    "Apartment 3": (43, 0.8),
    "Apartment 4": (50, 1.5),
    "Apartment 5": (42, 1.0),
    "Apartment 6": (48, 1.3),
    "Apartment 7": (46, 0.7),
    "Apartment 8": (44, 1.1),
    "Apartment 9": (52, 1.8),
    "Apartment 10": (40, 0.9),
    "Apartment 11": (49, 1.4),
    "Apartment 12": (45, 1.0),
    "Apartment 13": (47, 1.6),
    "Apartment 14": (41, 0.6),
    "Apartment 15": (53, 1.5),
    "Apartment 16": (46, 1.2),
    "Apartment 17": (44, 1.0),
    "Apartment 18": (51, 1.7),
    "Apartment 19": (43, 0.9),
    "Apartment 20": (48, 0.8),
    "Apartment 21": (45, 1.4),
    "Apartment 22": (50, 1.1),
    "Apartment 23": (42, 1.3),
    "Apartment 24": (47, 0.9),
    "Apartment 25": (49, 1.2)
}
k = 0
avr_a = 0
avr_km = 0
for name, (x, y) in apartments.items():
    if k < 2:
        plt.text(x, y, name)
        plt.scatter(x, y)
    if k >= 3:
        avr_a += x
        avr_km += y
    k += 1


avr_a = avr_a / 25
avr_km = avr_km / 25
plt.scatter(avr_a, avr_km)
print(avr_a,avr_km)

plt.xlabel("Area")
plt.ylabel("Distance to center (km)")
plt.title("Apartments")

plt.show()



