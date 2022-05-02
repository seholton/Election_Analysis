# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percenatge of votes each candidate won. 
# 4. The total number of votes each candidate won.
# 5. The winnder of the election base on popular vote. 

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0 # Initialize accumulater variable to zero
candidate_options = [] #new list that will hold candidate options
candidate_votes = {} #collection votes for each candidate.

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

total_county_votes = 0 # Initialize accumulater variable to zero
county_options = [] #new list that will hold county options
county_votes = {} #collection of votes per county

# Winning County and Winning County Tracker
winning_county_turnout= ""
winning_county = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
  
  # Go through rows and add value to total_votes and all_votes
             
    for row in file_reader:  
        total_votes += 1
        total_county_votes += 1
        # Print the candidate name and county name from each row
        candidate_name = row[2]
        county_name = row[1]

        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate option list
            candidate_options.append(candidate_name)

            # Begin tracking each candidates vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidates count
        candidate_votes[candidate_name] += 1
        
        if county_name not in county_options:
            # Add the county name to the county options list
            county_options.append(county_name)
            # Begin tracking each county's vote count
            county_votes[county_name] = 0
        # Add a vote to that county's vote count
        county_votes[county_name] += 1
    
        
with open(file_to_save, "w") as txt_file: # Oper and perpare to write on txt.file

    #print the final vote count to the terminal 
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
    print(election_results, end=" ")

    # Save the final vote cound to the text file
    txt_file.write(election_results)

    # Determine the percentage of votes for each county by looping through the counts.
    # Iterate through the county list.
    for county_name in county_votes:
        all_votes = county_votes[county_name]
        #calculate the percentage of votes
        county_percentage = float(all_votes) / float(total_county_votes) * 100
        # Print the county name and percentage and vote count.
        county_results = (f"{county_name}: {county_percentage:.1f}% ({all_votes:,})\n")          
        print(county_results)
        txt_file.write(county_results)


         # Determing what county had the high voter turnout
        if (all_votes > winning_county):
            #if true then set winning county = all_votes 
            winning_county = all_votes
            #set the winning county equal to the county's name
            winning_county_turnout = county_name
    
   
    winning_county_summary = (
    f"\n-------------------------\n"
    f"Largest County Turnout: {winning_county_turnout}\n"
    f"-------------------------\n\n")
    # Print a summary of results on the terminal and text file 
    print(winning_county_summary)
    txt_file.write(winning_county_summary)


    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate and county lists.
    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidate name and percentage and vote count.
        candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n\n") 
        print(candidate_results)
        txt_file.write(candidate_results)


        # Determing winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning count = votes and winning percentage = vote_perceptage
         winning_count = votes
         winning_percentage = vote_percentage
            #set the winning candidate equal to the candidate's name
         winning_candidate = candidate_name

    
    # Print summary of winning candidate on terminal and text file.
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
     
    txt_file.write(winning_candidate_summary)

   

 