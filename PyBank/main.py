#import os module to create a file path and to read a CSV file
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
#check the path
print(csvpath)

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

#Print to terminal and export to text file with the results
#Financial Analysis
#----------------------
#Total Months; XX
#Total: $XXXXX
#Average Change: $XXXX.XX
#Greatest Increase in Profits: Mon-Year ($XXXXXX)
#Greatest Decrease in Profits: Mon-Year ($XXXXXX)