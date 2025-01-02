import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42) 
x = np.random.rand(100)
y = np.random.rand(100)
sizes = np.random.rand(100) * 100  # Generate random sizes for the balls

plt.scatter(x, y, s=sizes, color='blue', alpha=0.7, edgecolors='k')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Random Ball Sizes')

plt.tight_layout()
plt.show()
