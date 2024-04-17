#written by Mayankita

import csv

file_path = 'sales.csv'

with open(file_path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(dict(row))

# Function to calculate mean of a list
def calculate_mean(data_list):
    return sum(data_list) / len(data_list)

# Initialize lists to collect numeric data from each column
sales = []
expenditure = []

# Reading the CSV file
with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        # Assuming 'sales' and 'expenditure' columns are integers
        sales.append(int(row['sales']))
        expenditure.append(int(row['expenditure']))

# Calculating means
mean_sales = calculate_mean(sales)
mean_expenditure = calculate_mean(expenditure)

# Calculating overall mean (average of both sales and expenditure means)
overall_mean = calculate_mean([mean_sales, mean_expenditure])

print(f"Mean Sales: {mean_sales}")
print(f"Mean Expenditure: {mean_expenditure}")
print(f"Overall Mean: {overall_mean}")