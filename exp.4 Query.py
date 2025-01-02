import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Date": [
        "2023-12-01", "2023-12-02", "2023-12-03", "2023-12-04", "2023-12-05",
        "2023-12-06", "2023-12-07", "2023-12-08", "2023-12-09", "2023-12-10"
    ],
    "Close": [140.5, 142.3, 143.8, 141.9, 145.2, 144.0, 147.3, 149.8, 148.6, 150.1]
}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])

start_date = "2023-12-03"
end_date = "2023-12-09"

filtered_data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

plt.figure(figsize=(10, 6))
plt.plot(filtered_data['Date'], filtered_data['Close'], marker='o', linestyle='-', color='blue')
plt.title('Alphabet Inc. Historical Stock Prices', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Close Price (USD)', fontsize=14)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
