import numpy as np
import matplotlib.pyplot as plt

math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.scatter(math_marks, science_marks, color='blue', alpha=0.7, edgecolors='k')

plt.xlabel('Mathematics Marks')
plt.ylabel('Science Marks')
plt.title('Comparison of Mathematics and Science Marks')

plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
