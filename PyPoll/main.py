# Import csv module
import csv
from pathlib import Path

# Set file path
csvpath = Path(__file__) /"..\Recources\election_data.csv"

# Set variables
total_votes = 0
candidate_votes = {}

# Open the CSV using the UTF-8 encoding
with open(csvpath,encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

     # Read the header row first
    csv_header = next(csvreader)

    # Find total number of votes
    for rows in csvreader:
        total_votes += 1

        # Find the count of all votes for each candidate
        candidate_name = rows[2]
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

# Find the winner
winner = max(candidate_votes, key=candidate_votes.get)


# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
# Print formatted results for each candidate
for candidate_name, vote_count in candidate_votes.items():
    percent_votes = vote_count / total_votes * 100  # This calculates the percentage each candidate got
    formatted_result = f"{candidate_name}: {percent_votes:.3f}% ({vote_count})"
    print(formatted_result)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Print the analysis to a txt file
output_file = Path(__file__) /"..\\analysis.txt"
# Open the file in write mode
with open(output_file, "w") as file:
    # Redirect the standard output (stdout) to the file
    import sys
    sys.stdout = file
    
    # Print results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
# Print formatted results for each candidate
    for candidate_name, vote_count in candidate_votes.items():
        percent_votes = vote_count / total_votes * 100  # This calculates the percentage each candidate got
        formatted_result = f"{candidate_name}: {percent_votes:.3f}% ({vote_count})"
        print(formatted_result)
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

# Reset the standard output to the console
sys.stdout = sys.__stdout__

# Notify the user that the output has been saved to the file
print(f"The financial analysis has been saved to '{output_file}'")