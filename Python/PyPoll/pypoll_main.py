# Modules
import os
import csv

# Set path for file
file = os.path.join("election_data.csv")

total_votes = 0
candidates_list = []
candidate_votes = {}
perc_per_candidate = []
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
        perc_per_candidate.append(vote_percentage_per_candidate)

        #gets winner candidate
        if (total_votes > winner_count):
            winner_count = total_votes
            winner_candidate = candidate
    #print winner_candidate = Khan 

#File to write results to
output_path = os.path.join("pypoll_output.txt")
#output_path = os.path.join("pypoll_output.csv")

#Whites results to output file
with open(output_path, "w") as csvfile:

    #Initialize file writers
    csvwriter = csv.writer(csvfile)

    #dictwriter = csv.DictWriter(csvfile),

    #Write the first row (header)
    content = 'Election Results\n'
    content = content + '----------------------------' + '\n'

    # csvfile.write('Election Results\n')
    # csvfile.write('----------------------------' + '\n')
    csvfile.write('Total Votes: ' + str(total_votes) + '\n')
            #print total_votes = 3521001
    csvfile.write('----------------------------' + '\n')
    i = 0

    # content = ""
    for candidate_name in candidate_votes:

        print(candidate_name)
        content = content + candidate_name + " : "

        votes = str(candidate_votes[candidate_name])
        content = content + votes + " : "
        print (votes) # votes

        percentage = str(perc_per_candidate[i])
        print (percentage) # percentages
        content = content + percentage + "%"

        i = i + 1 
        content = content + "\n"

        # print (str(candidates_list[candidate_name)) #not being nice
        #print("long thing : ", (str(candidates_list) + ": " + str(votes_per_candidate) + str(vote_percentage_per_candidate) + '%' + ')\n'))
        #csvfile.write(str(candidates_list[candidate_name] ":" + str(candidate_votes[candidate_name] ":" + str(perc_per_candidate[candidate_name]) + '\n')
            #print candidate_votes = {'Khan': 2218231, "O'Tooley": 105630, 'Correy': 704200, 'Li': 492940}
            #print vote_percentage_per_candidate = 63.0, 3.0, 20.0, 14.0
        #csvfile.write("Winner" + ":" + "winner_candidate" '\n')
            #print winner_candidate = Khan 
    csvfile.write(content)