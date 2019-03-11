# Modules
import os
import csv

# Set path for file
file = os.path.join("election_data.csv")

total_votes = 0
candidates_list = []
candidate_votes = {}
winner = ""
winner_count = 0  

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
    #print total_votes = 3521001
    #print candidate_votes = {'Khan': 2218231, "O'Tooley": 105630, 'Correy': 704200, 'Li': 492940}

    for candidate in candidate_votes:
        #calculates percentage of each candidate votes
        votes_per_candidate = candidate_votes.get(candidate)
        #print votes_per_candidate = 2218231, 105630, 704200, 492940
        vote_percentage_per_candidate = round(float(votes_per_candidate) / float(total_votes) * 100)
        #print vote_percentage_per_candidate = 63.0, 3.0, 20.0, 14.0

        #gets winner candidate
        if (total_votes > winner_count):
            winner_count = total_votes
            winner_candidate = candidate
    #print winner_candidate = Khan 

#File to write results to
output_path = os.path.join("pypoll_output.txt")
output_path = os.path.join("pypoll_output.csv")

#Whites results to output file
with open(output_path, "w") as csvfile:

    #Initialize file writers
    csvwriter = csv.writer(csvfile)

    dictwriter = csv.DictWriter(csvfile),

    #Write the first row (header)
    csvwriter.writerow('Election Results\n')
    csvwriter.writerow('----------------------------' + '\n')
    csvwriter.writerow('Total Votes: ' + str(total_votes) + '\n')
            #print total_votes = 3521001
    csvwriter.writerow('----------------------------' + '\n')
    for candidate in candidate_votes:
        dictwriter.writerow((candidate[0] + ": " + str(candidate[2]) + str(candidate[1]) '%' + ')\n')
            #print candidate_votes = {'Khan': 2218231, "O'Tooley": 105630, 'Correy': 704200, 'Li': 492940}
            #print vote_percentage_per_candidate = 63.0, 3.0, 20.0, 14.0
    csvwriter.writerow('Winner:' + winner_candidate + '\n')
            #print winner_candidate = Khan 

       
    