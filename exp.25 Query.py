import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.plot(x, y1, label='Line 1', color='blue', linewidth=2)

plt.plot(x, y2, label='Line 2', color='red', linewidth=3)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Plot with Multiple Lines, Different Widths and Colors')

plt.legend()

plt.show()
