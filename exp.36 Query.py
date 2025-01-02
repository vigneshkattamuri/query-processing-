import numpy as np
import matplotlib.pyplot as plt

group1_weights = [60, 62, 64, 66, 68]
group1_heights = [150, 155, 160, 165, 170]
group2_weights = [70, 72, 74, 76, 78]
group2_heights = [160, 165, 170, 175, 180]
group3_weights = [80, 82, 84, 86, 88]
group3_heights = [170, 175, 180, 185, 190]

plt.scatter(group1_weights, group1_heights, label='Group 1', color='blue', alpha=0.7, edgecolors='k')
plt.scatter(group2_weights, group2_heights, label='Group 2', color='green', alpha=0.7, edgecolors='k')
plt.scatter(group3_weights, group3_heights, label='Group 3', color='red', alpha=0.7, edgecolors='k')

plt.xlabel('Weights (kg)')
plt.ylabel('Heights (cm)')
plt.title('Comparison of Weights and Heights for Three Groups')

plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
