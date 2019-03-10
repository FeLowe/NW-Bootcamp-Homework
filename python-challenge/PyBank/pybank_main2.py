# Modules
import os
import csv

# Set path for file
file = os.path.join("budget_data.csv")

with open(file) as csvfile:
    csv_data = csv.reader(csvfile, delimiter=',')
    header_out = next(csv_data, None)

    month_count = 0
    month_list = []
    total_revenue = 0
    revenue_list = []

    

    for row in csv_data:
        month_count = month_count +1
        month_list.append(str(rwo[0])
    
    