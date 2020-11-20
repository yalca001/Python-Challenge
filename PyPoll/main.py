# Incorporated the csv module
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("PyPoll","Resources", "PyPoll_data.csv")
file_to_output = os.path.join("PyPoll","Analysis", "Results.txt")

# Set initial dictionary and counter 
candidate_dict = {}
total_votes = 0
pop_vote = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    #Skip the header row
    csv_header = next(csvreader)

    # Get the total number of votes
    for row in csvreader:
        total_votes += 1

        #If Candidate not already in candidate_dict, add candidate and givi them on vote
        if row[2] not in candidate_dict:
            candidate_dict[row[2]] = 1

            #If candidate already in candidate_dict, add one vote for the candidate
            else:
                candidate_dict[row[2]] += 1

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(f"Election Results\n")
    txt_file.write(f"----------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    # Loop through the key, value in candidate_dict and find the percentage of votes each candidate won
    for key, value in candidate_dict.items(): 
        percentage = "{:.3%}".format(value/total_votes)
        # Find the winner of the election based on popular vote 
        txt_file.write(f"{key}: {percentage} ({value})\n")
        if value > pop_vote:
            pop_vote = value
            winner = key
    txt_file.write(f"Winner: {winner}\n")
