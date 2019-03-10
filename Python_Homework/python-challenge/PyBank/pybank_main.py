# Modules
import os
import csv

# Set path for file
file = os.path.join("budget_data.csv")

months = []
prof_loss = []

with open(file) as csvfile:
    csv_data = csv.reader(csvfile, delimiter=',')
    header_out = next(csv_data, None)

    for row in csv_data:
        #Track Totals
        months.append(row[0])
        #print months
        
        prof_loss.append(int(row[1]))
        #print prof_loss

    total_months = len(months)

    gt_revenue_increase = prof_loss[0]
    gt_revenue_decrease = prof_loss[0]
    total_prof_loss = 0

    for row in range(len(prof_loss)):

        if prof_loss[row] >= gt_revenue_increase:
            gt_revenue_increase = prof_loss[row]
            print gt_revenue_increase
            gt_revenue_increase_month = months[row]
            print gt_revenue_increase_month

        elif prof_loss[row] < gt_revenue_decrease:
            gt_revenue_decrease = prof_loss[row]
            print gt_revenue_decrease        
            gt_revenue_decrease_month = months[row]
            print gt_revenue_decrease_month  

        total_prof_loss += prof_loss [row] 
    print total_prof_loss
     # Average Calculation       
average_change = (total_prof_loss / total_months) 
print average_change

# Specify the file to write to
output_path = os.path.join("pybank_output.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow('Financial Analysis\n')
    csvwriter.writerow('----------------------------' + '\n')
    # Write the second row
    csvwriter.writerow('Total Months: ' + str(total_months) + '\n')
    csvwriter.writerow('Total Revenue: $' + str(total_prof_loss) + '\n') 
    csvwriter.writerow('Average Revenue Change: $' + str(average_change) + '\n')
    csvwriter.writerow('Greatest Increase in Revenue: $ ' + str(gt_revenue_increase) + gt_revenue_increase_month)
    csvwriter.writerow('Greatest Decrease in Revenue: $'  + str(gt_revenue_decrease) + gt_revenue_decrease_month)
    
    

   
    





        