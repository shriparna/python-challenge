# main.py
# This program will cover the challenge for PyPoll
# Logic: 
# Read CSV file from Resources (Resources/election_data.csv).
# Create variable totalvotes and space as candidate
# Create an empty dictionary as we don't know how many candidates and also they may not be in the sorted order
# Create an empty list for output so that it can be printed on the console and written to the output file at the same time
# Traverse through the file and skip the header row
# Increement the counter of the votes in totalvotes
# Check if current candidate from file is not equal to candidate variable then make candidate variable from the candidate file and if the candidate not in dictionary then add the candidate and reset its value to zero
# while the candidate is same as candidate from file increment that candidate's count
# After the end of file 
# Append the candiate details from the dictionary
# Append the winner from the dictionary based on maximum votes
# Open the output file as CSV in anaysis/election_results.csv
# Print the values on the console
# Print the details in the output file

import csv

csvfilepath = "Resources/election_data.csv"
outfilepath = "analysis/election_results.csv"

totalvotes = 0
outputtext = []

candidate = ""
candictionary = {}
with open(csvfilepath, 'r') as pypollfile:
    csvreader = csv.reader (pypollfile, delimiter=',')

    csvheader = next(csvreader) # skip the title 

    # Append header to the output list
    outputtext.append("Election Results")
    outputtext.append("-------------------------")

    for row in csvreader:
        totalvotes = totalvotes + 1

        # Check if Candidate is changed
        if row[2] != candidate:
            candidate = row[2]
            if candidate not in candictionary: # new candidate
                candictionary[candidate]=0 # initialize value for new candidate
        candictionary[candidate] += 1

# Append the results to the output list
outputtext.append(f"Total Votes: {totalvotes}")
outputtext.append("-------------------------")
for key, value in candictionary.items():
    outputtext.append(f"{key}: {round(value/totalvotes*100, 3)} ({value})")
outputtext.append("-------------------------")
outputtext.append(f"Winner: {max(candictionary, key=candictionary.get)}")   
outputtext.append("-------------------------")

# Print values to the output file
with open(outfilepath, 'w') as outfile:

    # Initialize the csv.writer
    csvoutput = csv.writer(outfile)

    # There is no specific header as the output is more like a text format
    for line in outputtext:
        print(line)
        csvoutput.writerow([line])
