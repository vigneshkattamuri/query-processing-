import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Date": [
        "2023-12-01", "2023-12-02", "2023-12-03", "2023-12-04", "2023-12-05",
        "2023-12-06", "2023-12-07", "2023-12-08", "2023-12-09", "2023-12-10"
    ],
    "Volume": [1.5e6, 1.8e6, 1.6e6, 1.9e6, 2.1e6, 2.0e6, 1.7e6, 1.9e6, 2.2e6, 2.4e6]
}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])

start_date = "2023-12-03"
end_date = "2023-12-09"

filtered_data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

plt.figure(figsize=(10, 6))
plt.bar(filtered_data['Date'], filtered_data['Volume'], color='skyblue', width=0.6)
plt.title('Alphabet Inc. Trading Volume', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Trading Volume (in millions)', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
