# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The total number of votes each candidate won
# 4. The percentage of votes each candidate won
# 5. The winner of the election based on popular vote

# Add dependencies
import csv

# Create a file to load and file for output
file_to_load = 'C:\Files\election_results.csv'
file_to_save = 'C:\Files\Analysis\election.analysis.txt'

# Initialize the total vote counter
total_votes = 0

# Candidate options for list of candidates and candidate votes
candidate_options = []
candidate_votes = {}

# Track winning Candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_ptc = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    # Print each row 
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1
        # Candidate name from each row
        candidate_name = row [2]
        # If candidate does not match existing candidate then add it
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # begin tracking candidate votes
            candidate_votes[candidate_name] = 0
        # add vote to candidate's count
        candidate_votes[candidate_name] += 1

# Save results to text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------------\n")
    print(election_results, end="")
    
    # Save final vote count to text file
    txt_file.write(election_results)
    
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage
        votes = candidate_votes[candidate_name]
        vote_ptc = float (votes) / float(total_votes) * 100

        #Print each candidate name, vote ptc, and votes
        candidate_results = (f"{candidate_name}: {vote_ptc:.1f}% ({votes:,})\n")       
        print(candidate_results)
        # Save candidate results to text file
        txt_file.write(candidate_results)
        #Determine winning vote count, ptc, and candidate
        if (votes > winning_count) and (vote_ptc > winning_ptc):
            winning_count = votes
            winning_ptc = vote_ptc
            winning_candidate = candidate_name
            
            #Print winning candidate results    
    winning_candidate_summary = (
        f"----------------------------------\n"  
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Vote Percentage: {winning_ptc:.1f}%\n"
        f"----------------------------------\n") 
    print(winning_candidate_summary)
    # Save winning summary to text file
    txt_file.write(winning_candidate_summary) 
    
    

