#import os module to create a file path and to read a CSV file
import os
import csv
import string

#import the counter
from collections import Counter

#path
election_data = os.path.join('Resources', 'election_data.csv')

#THIS DIDN'T WORK AS WRITTEN, SO I'M KEEPING IT, BUT WANT TO TRY SOMETHING ELSE
#import the names of candidates (code from the resume analysis example)
#def load_file(filepath):
    #with open(filepath, "r") as votes_file_handler:
        #return votes_file_handler.read().lower().split()
# Grab the list of candidates
#candidate_list = load_file(election_data)
# Create a set of unique words from the resume
#candidates = set()
#print(candidates)
#END OF CODE THAT DIDN'T WORK

with open(election_data) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    votes_reader = csv.reader(csvfile, delimiter=',')
    candidates = []
    
    for row in votes_reader:
        candidate = row[2]

        candidates.append(candidate)
        print(candidates)

    # Read the header row first (skip this step if there is now header)
    votes_header = next(votes_reader)
    print(f"CSV Header: {votes_header}")

    #The total number of votes cast
    total_votes = len(list(votes_reader))
    print(total_votes)

#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

#is float helpful here? 

#Print to terminal and export to text file with the results
#summary = DataFrame({print("Election Results", 
# print("---------------------"),
# "Total Votes": [total_votes], 
# print("---------------------"), 
# "Candidates": [candidate_list],
# print("---------------------"),
# "Winner": [winner]
# print("---------------------")})

#FROM THE DIRECTIONS/EXAMPLE
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

#methodology
#open the file
#read the file
#read the third column [2] and store it as a list
#read that list to find the unique values
#create a list with the candidate list (unique values from column [2])
#count the number of times each name in the list occures in the column
#count the total number of rows
#create a dictionary with each candidates name, the % of the total votes they won, and their vote count
#print it out 
#create a txt files to print it out there