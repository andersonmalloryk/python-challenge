#import os module to create a file path and to read a CSV file
import os
import csv
import string
import collections

#import the counter
from collections import Counter

#path
election_data = os.path.join('Resources', 'election_data.csv')

#open file to read number of votes (maybe I can remove this once I figure out the counter)
with open(election_data) as csvfile:
    
    votes_reader = csv.reader(csvfile, delimiter=',')
    next(votes_reader)
    total_votes = len(list(votes_reader))

#open file to retrieve candidates
with open(election_data) as csvfile:
    votes_reader = csv.reader(csvfile, delimiter=',')
    next(votes_reader)
    candidates = []
    
    for row in votes_reader:   
        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)

votes = Counter(candidates)
with open(election_data) as input_file:
    for row in csv.reader(input_file, delimiter=','):
        votes[row[2]] += 1

print (candidates)
print(total_votes)
print (votes)

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