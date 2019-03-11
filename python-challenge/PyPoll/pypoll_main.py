# Modules
import os
import csv

# Set path for file
file = os.path.join("election_data.csv")

with open(file) as csvfile:
    csv_data = csv.reader(csvfile, delimiter=',')
    header_out = next(csv_data, None)