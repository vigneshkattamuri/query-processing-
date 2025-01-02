import pandas as pd

# Data for the table
data = [
    [2.456, -1.234, 0.567, 3.789],
    [-0.987, 4.321, -2.654, 1.109],
    [3.210, 0.876, -0.321, -4.567],
    [-1.765, -3.421, 2.987, 0.654],
    [0.543, 2.109, 1.234, -2.987],
    [-4.321, 1.765, 0.987, 3.210],
    [1.109, -2.654, -3.789, 0.876],
    [2.987, 0.654, 4.567, -1.234],
    [-3.789, 3.210, 1.765, 2.654]
]

# Create the DataFrame
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

# Function to apply color formatting
def highlight_negative_values(val):
    color = 'blue' if val < 0 else 'black'
    return f'color: {color}'

# Apply the function to each column of the DataFrame using apply
styled_df = df.style.applymap(highlight_negative_values)

# Display the styled DataFrame (works in Jupyter notebook)
styled_df
