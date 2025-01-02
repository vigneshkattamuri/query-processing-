import matplotlib.pyplot as plt

file_name = r"C:\Users\Greeshma Sri\Downloads\test.txt"

x = []
y = []

with open(file_name, "r") as file:
    for line in file:
        values = line.split()
        x.append(float(values[0]))
        y.append(float(values[1]))

plt.plot(x, y, marker="o", label="Line from File")

plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Line Plot from Text File")

plt.legend()

plt.show()

