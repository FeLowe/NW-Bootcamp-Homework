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

#"Voter ID(row[0])	County(row[1])	Candidate"(row[2])
    for row in csv_data:
        #counts total votes
        total_votes = total_votes +1

       #gets candidate name at "Candidate" column
        candidate_name = row[2]
    #loops through all cadidate names in cadidates list and calculates candidate votes    
    if candidate_name not in candidates_list:
        candidates_list.append(candidate_name)
        candidate_votes[candidate_name] = 0
    candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        
    print candidate_votes    