# Modules
import os
import csv

# Set path for file
file = os.path.join("election_data.csv")

total_votes = 0
candidates_list = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0  

with open(file) as csvfile:
    csv_data = csv.reader(csvfile, delimiter=',')
    header_out = next(csv_data, None)
  
# -----------------------------------    
    #loops through each row in the csv file
    for row in csv_data:

        #adds each vote to the total_votes
        total_votes = total_votes + 1 

        #gets candidate name at "Candidate" column row[2]
        candidate_name = row[2]

        #checks if the candidate name is not in cadidate list.
        if candidate_name not in candidates_list:

            #adds candidate name to candidate list
            candidates_list.append(candidate_name)

            #counts candidate votes by name
            candidate_votes[candidate_name] = 0

        #adds a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
    #print candidate_votes
    print total_votes