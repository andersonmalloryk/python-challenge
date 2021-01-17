#import os module to create a file path and to read a CSV file
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
#check the path
print(csvpath)

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

#Print to terminal and export to text file with the results
#Election Results
#----------------------
#Total Votes: XXXXXXXX
#----------------------
#Khan: XX.XXX% (XXXXXXXX)
#Corey: XX.XXX% (XXXXXXX)
#li:  XX.XXX% (XXXXXXX)
#O'Tooley:  XX.XXX% (XXXXXXX)
#----------------------
#Winner: NAME
#----------------------