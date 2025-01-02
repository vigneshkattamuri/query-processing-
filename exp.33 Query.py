import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42) 
x = np.random.rand(100)
y = np.random.rand(100)

plt.scatter(x, y, facecolors='none', edgecolors='blue', alpha=0.7)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of Random Distribution (Empty Circles)')

plt.tight_layout()
plt.show()
