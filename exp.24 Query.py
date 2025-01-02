import pandas as pd
import matplotlib.pyplot as plt

file_name = r"C:\Users\Greeshma Sri\Downloads\fdata [MConverter.eu].csv"

data = pd.read_csv(file_name)

print("Columns in the file:", data.columns)

data.columns = data.columns.str.strip()

data['Date'] = pd.to_datetime(data['Date'], format='%m-%d-%y')

plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Open'], marker='o', label='Open Price')
plt.plot(data['Date'], data['High'], marker='o', label='High Price')
plt.plot(data['Date'], data['Low'], marker='o', label='Low Price')
plt.plot(data['Date'], data['Close'], marker='o', label='Close Price')

plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('Alphabet Inc. Financial Data (Oct 3, 2016 - Oct 7, 2016)')

plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
