#written by Humaira

import csv

def write_summary(total_sales):
    with open (' sales_summary.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(['Year', 'Total Sales'])
        # Write data rows
        writer.writerow(['2018', total_sales])
        print ("Summary of results has been written to sales_summary.csv")

write_summary(2300)
