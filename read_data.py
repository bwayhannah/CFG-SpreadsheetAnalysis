import csv

def read_data(file_name): #reads csv file and outputs as a list of dictionaries where each key is column heading 
    data = []

    with open(file_name,'r') as my_csv:
        spreadsheet = csv.DictReader(my_csv)
        for row in spreadsheet:
            data.append(row)

    return data


# data = read_data('sales.csv')
# print(data)