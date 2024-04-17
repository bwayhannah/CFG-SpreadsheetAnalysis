from read_data import read_data
import pandas as pd

def monthly_change(heading):
    data = read_data('sales.csv')
    df = pd.DataFrame(data) #create pandas dataframe
    df2 = pd.DataFrame(df[heading].astype(float).pct_change()*100) #create new dataframe with pct change column
    df2.rename(columns={heading: heading + ' change (%)'}, inplace=True) #rename the headers

    return df, df2

df, df2 = monthly_change('sales') 
df3, df4 = monthly_change('expenditure')
dataframes = [df, df2, df4] #make a list of dataframes want to add together
result = pd.concat(dataframes, axis=1) #concatanate old df with new columns
print(result)