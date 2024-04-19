import pandas as pd
from read_data import read_data


def return_max(file_name, heading, corresponds): #reads the data and returns the max_value and corresponding month/name the max occurred
    # df2 = max_values(file_name, heading)
    data = read_data(file_name)

    df = pd.DataFrame(data) 
    #converts the data into a pandas DataFrame

    df2 = df[df[heading].values == df[heading].values.max()].reset_index(drop=True)
    #makes a new dataframe from df with all of the values equal to the max value and resets the indices
    max_names = []
    for index, row in df2.iterrows(): #iterate over each row of the dataframe
        max_value = row[heading] 
        max_name = str(row[corresponds])
        max_names.append(max_name)
        names_str = str(max_names)[1:-1] #write as a string with slice to remove []
    return heading, max_value, names_str

def return_min(file_name, heading, corresponds): #reads the data and returns the min_value and corresponding month/namethe min occurred
    # df2 = min_values(file_name, heading)
    data = read_data(file_name)

    df = pd.DataFrame(data) 
    #converts the data into a pandas DataFrame

    df2 = df[df[heading].values == df[heading].values.min()].reset_index(drop=True)
    #makes a new dataframe from df with all of the values equal to the min value and resets the indices

    min_names = []
    for index, row in df2.iterrows(): #iterate over each row of the dataframe
        min_value = row[heading] 
        min_name = str(row[corresponds])
        min_names.append(min_name)
        names_str = str(min_names)[1:-1] #write as a string with slice to remove []
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