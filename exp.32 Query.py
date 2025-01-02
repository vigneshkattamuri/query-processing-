import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)  # For reproducibility
x = np.random.rand(100)
y = np.random.rand(100)

plt.scatter(x, y, color='blue', alpha=0.7, edgecolors='k')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of Random Distribution')

plt.tight_layout()
plt.show()
