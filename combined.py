import csv
import pandas as pd

def read_data(file_name): #reads csv file and outputs as a list of dictionaries where each key is column heading 
    data = []

    with open(file_name,'r') as my_csv:
        spreadsheet = csv.DictReader(my_csv)
        for row in spreadsheet:
            data.append(row)

    return data

def max_values(file_name, heading): #extracts the max values for a column as a new dataframe
    data = read_data(file_name)

    df = pd.DataFrame(data) 
    #converts the data into a pandas DataFrame

    df2 = df[df[heading].values == df[heading].values.max()].reset_index(drop=True)
    #makes a new dataframe from df with all of the values equal to the max value and resets the indices

    return df2

def min_values(file_name, heading): #extracts the min values for a column as a new dataframe
    data = read_data(file_name)

    df = pd.DataFrame(data) 
    #converts the data into a pandas DataFrame

    df2 = df[df[heading].values == df[heading].values.min()].reset_index(drop=True)
    #makes a new dataframe from df with all of the values equal to the max value and resets the indices

    return df2


def return_max(file_name, heading): #takes the dataframe from max_values and returns the max_value and date the max occurred
    df2 = max_values(file_name, heading)
    max_dates = []
    for index, row in df2.iterrows():
        max_value = row[heading]
        max_date = str(row['month']) + ' ' + str(row['year'])
        max_dates.append(max_date)
        dates_str = str(max_dates)[1:-1]
    return heading, max_value, dates_str


def return_min(file_name, heading): #takes the dataframe from min_values and returns the min_value and date the min occurred
    df2 = min_values(file_name, heading)
    min_dates = []
    for index, row in df2.iterrows():
        min_value = row[heading]
        min_date = str(row['month']) + ' ' + str(row['year'])
        min_dates.append(min_date)
        dates_str = str(min_dates)[1:-1]
    return heading, min_value, dates_str


heading, min_value, dates_str = return_min('IMDB_Top_250_Movies.csv', 'rating')
print(f'Lowest value of {heading}: {min_value}, corresponding date(s): {dates_str}')

# heading, max_value, dates_str = return_max('sales.csv', 'sales')
# print(f'Lowest value of {heading}: {max_value}, corresponding date(s): {dates_str}')