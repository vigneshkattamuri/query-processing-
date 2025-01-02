import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': ['01-04-2020', '02-04-2020', '03-04-2020', '06-04-2020', '07-04-2020', '08-04-2020', 
             '09-04-2020', '13-04-2020', '14-04-2020', '15-04-2020', '16-04-2020', '17-04-2020',
             '20-04-2020', '21-04-2020', '22-04-2020', '23-04-2020', '24-04-2020', '27-04-2020', 
             '28-04-2020', '29-04-2020', '30-04-2020', '01-05-2020'],
    'Stock Price': [1105.62, 1120.84, 1097.88, 1186.92, 1186.51, 1210.28, 1211.45, 1217.56, 1269.23, 
                    1262.47, 1263.47, 1283.25, 1266.61, 1216.34, 1263.21, 1276.31, 1279.31, 1275.88, 
                    1233.67, 1341.48, 1348.66, 1320.61],
    'Volume': [2343100, 1964900, 2313400, 2664700, 2387300, 1975100, 2175400, 1739800, 2470400, 
               1671700, 2518100, 1949000, 1695500, 2153000, 2093100, 1566200, 1640400, 1600600, 
               2951300, 3793600, 2665400, 2072500]
}

alphabet_stock_data = pd.DataFrame(data)

alphabet_stock_data['Date'] = pd.to_datetime(alphabet_stock_data['Date'], format='%d-%m-%Y')

start_date = '2020-04-01'
end_date = '2020-04-30'

filtered_data = alphabet_stock_data[(alphabet_stock_data['Date'] >= start_date) & 
                                    (alphabet_stock_data['Date'] <= end_date)]

plt.figure(figsize=(10, 6))
plt.scatter(filtered_data['Volume'], filtered_data['Stock Price'], alpha=0.6, color='b')
plt.title('Alphabet Inc. Stock Price vs Trading Volume (April 2020)')
plt.xlabel('Trading Volume')
plt.ylabel('Stock Price (USD)')
plt.grid(True)
plt.show()
