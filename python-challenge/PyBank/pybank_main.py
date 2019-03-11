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
        # push each month to months list
        months.append(row[0])
        # push each value to prof_loss
        prof_loss.append(int(row[1]))
    #gets len of months, print single count number as it is oulside the loop. 
    total_months = len(months)
    
    #set variables to start at 0 value
    gt_revenue_increase = prof_loss[0]
    gt_revenue_decrease = prof_loss[0]
    total_prof_loss = 0
    
    #loop through each row in prof_loss list 
    for row in range(len(prof_loss)):

        #gets greatest revenue increse value and month
        if prof_loss[row] >= gt_revenue_increase:
            gt_revenue_increase = prof_loss[row]
            gt_revenue_increase_month = months[row]
        #gets greatest revenue descrease value and month
        elif prof_loss[row] < gt_revenue_decrease:
            gt_revenue_decrease = prof_loss[row]      
            gt_revenue_decrease_month = months[row]
        
        #get total revenuw
 total_prof_loss += prof_loss [row] 
    
#Average calculation       
average_change = round(total_prof_loss / total_months,2) 

#File to write results to
utput_path = os.path.join("pybank_output.txt")
output_path = os.path.join("pybank_output.csv")


# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path,'w') as csvfile:


    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)

    # Write the first row (column headers)
    csvwriter.writerow('Financial Analysis\n')
    csvwriter.writerow('----------------------------' + '\n')
    # Write the second row forwards
    csvwriter.writerow('Total Months: ' + str(total_months) + '\n')
    csvwriter.writerow('Total: $' + str(total_prof_loss) + '\n') 
    csvwriter.writerow('Average Change: $' + str(average_change) + '\n')
    csvwriter.writerow('Greatest Increase in Profits: $ ' + str(gt_revenue_increase) + gt_revenue_increase_month)
    csvwriter.writerow('Greatest Decrease in Profits: $' + str(gt_revenue_decrease) + gt_revenue_decrease_month)
    
    

   
    





        