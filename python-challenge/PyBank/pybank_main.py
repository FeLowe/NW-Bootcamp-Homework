# Modules
import os
import csv

# Set path for file
file = os.path.join("budget_data.csv")

months = []
total_revenue = []
total_revenue_sum = 0

with open(file) as csvfile:
    csv_data = csv.reader(csvfile, delimiter=',')
    header_out = next(csv_data, None)

    for row in csv_data:
        # push each month to months list
        months.append(row[0])
        # push each value to prof_loss
        total_revenue.append(int(row[1]))
    #gets len of months, print single count number as it is oulside the loop. 
    total_months = len(months)
    #print(total_revenue)
    #sets variables to start at 0 value
    gt_revenue_increase = total_revenue[0]
    gt_revenue_decrease = total_revenue[0]
    #print (gt_revenue_decrease)
    #print (gt_revenue_decrease)
    
    #loops through each row in total_revenue list 
    for row in range(0,len(total_revenue)):

        #gets greatest revenue increse value and month
        if total_revenue[row] >= gt_revenue_increase:
            gt_revenue_increase = total_revenue[row]
            #print(gt_revenue_increase)
            gt_revenue_increase_month = months[row]
        #gets greatest revenue descrease value and month
        elif total_revenue[row] < gt_revenue_decrease:
            gt_revenue_decrease = total_revenue[row]      
            gt_revenue_decrease_month = months[row]
        
        #gets total revenue
    total_revenue_sum = total_revenue_sum + total_revenue[row]
    #print (total_revenue_sum)
  
#Average calculation       
average_change = round(sum(total_revenue) / len(months),2) 

print(total_months)
print(total_revenue_sum)
print(average_change)
print(gt_revenue_increase)
print(gt_revenue_decrease)
print(gt_revenue_increase_month)
print(gt_revenue_decrease_month)
#File to write results to
output_path = os.path.join("pybank_output.txt")
#output_path = os.path.join("pybank_output.csv")


# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path,'w') as csvfile:


    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)

    # Write the first row (column headers)
    csvwriter.writerow('Financial Analysis\n')
    csvwriter.writerow('----------------------------' + '\n')
    # Write the second row forwards
    csvwriter.writerow('Total Months: ' + str(total_months) + '\n')
    csvwriter.writerow('Total: $' + str(total_revenue_sum) + '\n') 
    csvwriter.writerow('Average Change: $' + str(average_change) + '\n')
    csvwriter.writerow('Greatest Increase in Profits: $ ' + str(gt_revenue_increase) + gt_revenue_increase_month)
    csvwriter.writerow('Greatest Decrease in Profits: $' + str(gt_revenue_decrease) + gt_revenue_decrease_month)
    


   
    





        