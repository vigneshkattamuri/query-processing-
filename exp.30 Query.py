import matplotlib.pyplot as plt
import numpy as np

means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]

x = np.arange(len(means_men)) 
width = 0.35  
fig, ax = plt.subplots(figsize=(8, 6))

bars_men = ax.bar(x - width/2, means_men, width, label='Men', color='blue')
bars_women = ax.bar(x + width/2, means_women, width, label='Women', color='red')

ax.set_xlabel('Groups')
ax.set_ylabel('Scores')
ax.set_title('Scores by Group and Gender')
ax.set_xticks(x)
ax.set_xticklabels(['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5'])
ax.legend()

plt.show()
