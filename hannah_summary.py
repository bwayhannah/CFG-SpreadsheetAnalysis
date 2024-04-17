from max_and_min import return_max, return_min
import csv

def write_summary(file_name, heading):
    heading, max_value, max_dates_str = return_max(file_name, heading)
    with open (' sales_summary.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow([f'Max {heading}', 'Date'])
        # Write data rows
        writer.writerow([max_value, max_dates_str])
        print ("Summary of results has been written to sales_summary.csv")

write_summary('sales.csv', 'sales')
