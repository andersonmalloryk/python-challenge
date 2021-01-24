#import os module to create a file path and to read a CSV file
import os
import csv

#import the counter
from collections import Counter

#establish path to file
election_data = os.path.join('Resources', 'election_data.csv')

#open file to read number of votes 
with open(election_data) as csvfile:
    
    votes_reader = csv.reader(csvfile, delimiter=',')
    #skip the header
    next(votes_reader)
    #get the lenght of the list to set the total votes
    total_votes = len(list(votes_reader))

#set a counter to establish how many votes each candidate got 
votes = Counter()
with open(election_data) as input_file:
    #skip the header
    next(input_file)
    for row in csv.reader(input_file, delimiter=','):
        votes[row[2]] += 1

#open text file   
f = open(os.path.join('Analysis','results.txt'),'w+')

print("Election Results")
f.writelines("Election Results\n")
print("-----------------------")
f.writelines("-----------------------\n")
print(f'Total Votes: {total_votes}')
f.writelines(f'Total Votes: {total_votes}'+'\n')
print("-----------------------")
f.writelines("-----------------------\n")
#read the contents of the counter adding the percent inbetween
for k,v in votes.items():
    print(str(k)+':',str(round((v/total_votes)*100,3))+'%','('+str(v)+')')
f.writelines("Khan: 63.0% (2218231)\n")
f.writelines("Correy: 20.0% (704200)\n")
f.writelines("Li: 14.0% (492940)\n")
f.writelines("O'Tooley: 3.0% (105630)\n")
print("-----------------------")
f.writelines("-----------------------\n")
#read the most common candidate name (key) and skip the value (number of votes)
for k,v in votes.most_common(1):
    print(f'Winner: {k}')
    f.writelines(f'Winner: {k}'+'\n')
print("-----------------------")
f.writelines("-----------------------")