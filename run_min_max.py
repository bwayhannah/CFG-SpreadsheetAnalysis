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
    #makes a new dataframe from df with all of the values equal to the min value and resets the indices

    return df2


def return_max(file_name, heading, corresponds): #takes the dataframe from max_values and returns the max_value and date the max occurred
    df2 = max_values(file_name, heading)
    max_names = []
    for index, row in df2.iterrows():
        max_value = row[heading]
        max_name = str(row[corresponds])
        max_names.append(max_name)
        names_str = str(max_names)[1:-1]
    return heading, max_value, names_str


def return_min(file_name, heading, corresponds): #takes the dataframe from min_values and returns the min_value and date the min occurred
    df2 = min_values(file_name, heading)
    min_names = []
    for index, row in df2.iterrows():
        min_value = row[heading]
        min_name = str(row[corresponds])
        min_names.append(min_name)
        names_str = str(min_names)[1:-1]
    return heading, min_value, names_str


# heading, min_value, names_str = return_min('sales.csv', 'sales', 'month')
# print(f'Lowest {heading}: {min_value}, corresponding month(s): {names_str}')

# heading, max_value, names_str = return_max('sales.csv', 'sales', 'month')
# print(f'Highest {heading}: {max_value}, corresponding month(s): {names_str}')


# heading, min_value, names_str = return_min('sales.csv', 'expenditure', 'month')
# print(f'Lowest {heading}: {min_value}, corresponding month(s): {names_str}')

# heading, max_value, names_str = return_max('sales.csv', 'expenditure', 'month')
# print(f'Highest {heading}: {max_value}, corresponding month(s): {names_str}')



#using the script for a different csv file

# heading, min_value, names_str = return_min('IMDB.csv', 'rating', 'name')
# print(f'Lowest {heading}: {min_value}, corresponding movie(s): {names_str}')

# heading, max_value, names_str = return_max('IMDB.csv', 'rating', 'name')
# print(f'Highest {heading}: {max_value}, corresponding movie(s): {names_str}')