import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
y3 = [1, 4, 9, 16, 25]
y4 = [5, 7, 11, 13, 17]

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, y1, label='Line 1', color='blue')
axs[0, 0].set_title('Plot 1')
axs[0, 0].set_xlabel('X Axis')
axs[0, 0].set_ylabel('Y Axis')
axs[0, 0].legend()

axs[0, 1].plot(x, y2, label='Line 2', color='green')
axs[0, 1].set_title('Plot 2')
axs[0, 1].set_xlabel('X Axis')
axs[0, 1].set_ylabel('Y Axis')
axs[0, 1].legend()

axs[1, 0].plot(x, y3, label='Line 3', color='red')
axs[1, 0].set_title('Plot 3')
axs[1, 0].set_xlabel('X Axis')
axs[1, 0].set_ylabel('Y Axis')
axs[1, 0].legend()

axs[1, 1].plot(x, y4, label='Line 4', color='purple')
axs[1, 1].set_title('Plot 4')
axs[1, 1].set_xlabel('X Axis')
axs[1, 1].set_ylabel('Y Axis')
axs[1, 1].legend()

plt.tight_layout()

plt.show()
