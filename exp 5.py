import pandas as pd

def sundays_of_year(year):

    start_date = f'{year}-01-01'
    end_date = f'{year}-12-31'
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    

    sundays = date_range[date_range.dayofweek == 6]
    
    return sundays


year = 2024
sundays = sundays_of_year(year)
print(f"Sundays in {year}:\n", sundays)
