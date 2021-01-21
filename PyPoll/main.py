#import os module to create a file path and to read a CSV file
import os
import csv

#import the counter
from collections import Counter

#path
election_data = os.path.join('Resources', 'election_data.csv')

#open file to read number of votes (maybe I can remove this once I figure out the counter)
with open(election_data) as csvfile:
    
    votes_reader = csv.reader(csvfile, delimiter=',')
    next(votes_reader)
    total_votes = len(list(votes_reader))

votes = Counter()
with open(election_data) as input_file:
    next(input_file)
    for row in csv.reader(input_file, delimiter=','):
        votes[row[2]] += 1


print("Election Results")
print("-----------------------")
print(f'Total Votes {total_votes}')
print("-----------------------")
print(votes)
print("-----------------------")

print("-----------------------")

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
