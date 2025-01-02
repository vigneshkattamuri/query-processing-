import numpy as np
import matplotlib.pyplot as plt

means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]
std_men = [4, 3, 4, 1, 5]
std_women = [3, 5, 2, 3, 3]

labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
x = np.arange(len(labels))

width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x, means_men, width, yerr=std_men, label='Men', color='skyblue', capsize=5)

rects2 = ax.bar(x, means_women, width, yerr=std_women, bottom=means_men, label='Women', color='lightcoral', capsize=5)

ax.set_xlabel('Groups')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.tight_layout()
plt.show()
