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
    current_revenue_value = 0
    previous_revenue_value = 0
    calculated_revenue_list = []
    

    for row in csv_data:

        month_list.append(row[0])
        month_count = len(month_list)
        revenue_list.append(row[1])

        for row in range(len(revenue_list)):
            
            if current_revenue_value != 0
            print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])

            # BONUS: Set variable to confirm we have found the video
            found = True

            # BONUS: Stop at first results to avoid duplicates
            break
            current_revenue_value = revenue_list[row[0]]

            #if revenue_list[row] >= gt_revenue_increase:
            #gt_revenue_increase = prof_loss[row]
            #gt_revenue_increase_month = months[row]
            #print gt_revenue_increase_month

            #elif prof_loss[row] < gt_revenue_decrease:
            #gt_revenue_decrease = prof_loss[row]
            #print gt_revenue_decrease        
            #gt_revenue_decrease_month = months[row]
            #print gt_revenue_decrease_month  

        #total_prof_loss += prof_loss [row] 
    #print total_prof_loss
        #current_revenue_value = int(row[1])
    
        #calculated_revenue_value = current_revenue_value - previous_revenue_value
        #calculated_revenue_list.append(calculated_revenue_value)

        #average_change = (sum(revenue_list) / month_count) 
        

