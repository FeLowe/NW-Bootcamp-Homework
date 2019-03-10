#import modules
import os
import csv
#create trackers
totalMonths = 0
totalRev = 0
pastRev = 0
highestIncRev = 0
lowestDecRev = 99999999999
#create lists to store revenue change
revChange = []
#create path
budget_csvpath = os.path.join('budget_data.csv')
#print(budget_csvpath)
#read csv file
with open(budget_csvpath) as csvfile:
    budget_csvreader = csv.reader(csvfile, delimiter=',')
    #print(budget_csvreader)
    next(budget_csvreader, None)
    for row in budget_csvreader:
        #count total months in csv file
        totalMonths = totalMonths + 1
        #print totalMonths
        #count total revenue in csv file
        totalRev = totalRev + (int(row[1]))
        #print totalRev
        #create a variable that will count the revenue change
        monthlyRevChange = int(row[1]) - pastRev
        pastRev = int(row[1])
        #add changes in new list
        revChange.append(monthlyRevChange)
        print(monthlyRevChange)
        #calculate the average change in revenue
        avgRevChange = round(sum(revChange)/totalMonths)
        #print(avgRevChange)
        #find the greatest increase in revenue
        if (monthlyRevChange > highestIncRev):
            highestIncMonth = row[0]
            highestIncRev = monthlyRevChange 
        #find the greatest decrease in revenue
        if (monthlyRevChange < lowestDecRev):
            lowestDecMonth = row[0]
            lowestDecRev = monthlyRevChange

            # Specify the file to write to
output_path = os.path.join("test_pybank_output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)
    
    csvwriter.writerow('Financial Analysis\n')
    csvwriter.writerow('----------------------------' + '\n')
    # Write the second row
    csvwriter.writerow('Total Months: ' + str(totalMonths) + '\n')
    csvwriter.writerow('Total: $' + str(totalRev) + '\n') 
    csvwriter.writerow('Average Change: $' + str(avgRevChange) + '\n')
    csvwriter.writerow('Greatest Increase in Profits: $ ' + str(highestIncMonth) + str(highestIncRev + '\n')
    csvwriter.writerow('Greatest Decrease in Profits: $'  + str(lowestDecMonth) + str(lowestDecRev))
