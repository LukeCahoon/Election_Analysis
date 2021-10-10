# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who recieved votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

# Add our dependencies.
import csv

# Assign a variable for the file to load and the path.
file_to_load = 'C:/Users/Work/Desktop/Classwork Desktop Files/Election Analysis/Resources/election_results.csv'
# Create a filename variable to a direct or indirect path to the file.
file_to_save = 'C:/Users/Work/Desktop/Classwork Desktop Files/Election Analysis/Election_Analysis/election_analysis.txt'

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

