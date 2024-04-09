from read_data import read_data
import pandas as pd

def monthly_change(heading):
    data = read_data('sales.csv')
    df = pd.DataFrame(data)
    df2 = pd.DataFrame(df[heading].astype(float).pct_change()*100)
    df2.rename(columns={heading: heading + ' change (%)'}, inplace=True)

    return df, df2

df, df2 = monthly_change('sales')
df3, df4 = monthly_change('expenditure')
frames = [df, df2, df4]
result = pd.concat(frames, axis=1)
print(result)