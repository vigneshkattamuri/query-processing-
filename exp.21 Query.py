import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Catherine"],
    "Occupation": ["Engineer", "Doctor", "Artist"]
}
df = pd.DataFrame(data)

def swap_case(df, column_name):
    if column_name in df.columns:
        df[column_name] = df[column_name].apply(lambda x: x.swapcase())
    else:
        print(f"Column '{column_name}' does not exist in the DataFrame.")
    return df

column_to_swap = "Occupation"

result_df = swap_case(df, column_to_swap)

print(result_df)
