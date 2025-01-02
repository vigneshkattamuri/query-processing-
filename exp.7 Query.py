import pandas as pd

sales_data = {
    'Item': ['Item A', 'Item B', 'Item A', 'Item C', 'Item B', 'Item C'],
    'Sale Value': [100, 200, 150, 50, 250, 75],
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06']
}

df = pd.DataFrame(sales_data)

pivot_table = df.pivot_table(values='Sale Value', index='Item', aggfunc=['max', 'min'])

print(pivot_table)
