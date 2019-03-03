## PyPoll
#--------------------------------------------------------------------------------------
  # [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: 
  # The dataset is composed of two columns:`Voter ID`, `County`, and `Candidate`. 
#--------------------------------------------------------------------------------------
 
# Python script that analyzes the records to calculate each of the following:

# Dependencies
import os
import csv

# Path to collect data from the Resources folder, adjust appropriately
csvpath = "C:/Users/boninjv/Desktop/python-challenge/PyPoll/Resources/election_data.csv"

# Declare in Memory Variables 
row_count=0
winning_number_of_votes = 0
voter_id = []
county = []
candidate = []
unique_candidates = []

# Path to save results to the Resources folder, adjust appropriately
f= open("Resources/election_analysis.txt","w+")

# Read data from the Resources folder
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    # Loop through the rows of *.csv
    for row in csvreader:
            
            # Complete a list of candidates who received votes
            row_count = row_count+1
            voter_id.append(row[0])
            county.append(row[1])
            candidate.append(row[2])
            current_candidate = row[2]
            # Combine and create a list of candidates who received votes
            if unique_candidates.count(current_candidate) == 0:
                unique_candidates.append(current_candidate)
    
    print(f"-------------------------")
    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes : {row_count}")
    string = "Total Votes : "+ str(row_count)
    print(f"-------------------------")
    f.write('Election Results\n')
    f.write("------------------------")
    f.write(string + '\n')
    f.write('------------------------\n')

    # Loop through the rows of *.csv list of unique candidates to find the winner
    for person in unique_candidates:
       
        number_of_votes = candidate.count(person)

        if number_of_votes > winning_number_of_votes:
                winner = person
                winning_number_of_votes = number_of_votes
        
        percent_of_votes = number_of_votes / row_count *100
        percent_of_votes = round(percent_of_votes,4)
        
        print(f"{person} : {percent_of_votes}% ({number_of_votes})  ")
        string = str(person) + " :   " + "   " + str(percent_of_votes) + "%" + "   " + "(" + str(number_of_votes) + ")"
        f.write(string+"\n")

print(f"-------------------------")
f.write('------------------------\n')
print(f"Winner : {winner}")
string = "Winner  :  " +str(winner)
f.write(string+"\n")
f.write('------------------------\n')
f.close

#'--------------------------------------------------------------------------------------
# Template
  #```text
  #Election Results
  #-------------------------
  #Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
  #-------------------------
  #```
#'--------------------------------------------------------------------------------------