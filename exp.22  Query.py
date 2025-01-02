import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, label="y = 2x", color="blue", linestyle="-", marker="o")

plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Line Plot Example")

plt.legend()

plt.show()
