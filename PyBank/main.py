#import os module to create a file path and to read a CSV file
import os
import csv
#do I need to import string

budget_data = os.path.join('Resources', 'budget_data.csv')
#check the path
print(budget_data)

#add a container for the change column to be added to calculate average change of profit and losses
profit_loss_change = []

with open(budget_data, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    budget_reader = csv.DictReader(csvfile, delimiter=',')

    # Read the header row first 
    budget_header = next(budget_reader)
    print(f"CSV Header: {budget_header}")

    #IT WORKS  when the month counter is in this location

    for row in budget_reader:
        month = row["Date"]
        profit_loss = row["Profit/Losses"]     
        #add profit_loss_change - can't get this to work get a syntax error
        #change = profit_loss.pct_change()
        profit_loss_change.apend(
            {
                "month": row["Date"],
                "profit_loss": row["Profit/Losses"],
                "change": change
            }
        )

#pull file name from original path
_, filename = os.path.split(filepath)

#write to the original file adding the change column
csvpath = os.path.join("output", filename)
with open(csvpath, "w") as csvfile:
    fieldnames = ["month", "profit_loss", "change"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(profit_loss_change)

#appended_budget = os.path.join("budget_data_change.csv")
#with open(appended_budget, "w", newline="") as datafile:
    #writer = csv.write(datafile)
    #writer.writerow("profit_loss_change")

    #writer.writerows(appended_budget)

    #The total number of months included in the dataset
    month_count = len(list(budget_reader))
    print(month_count)   
        
        #for row in budget_reader:

        #attempt at calculating change.... NEEDS HELP
        #profit_loss_change = f"{row}-{row + 1}"
        #profit_loss_change.apend({"month": row["Date"],"profit_loss": row:["Profit/Losses"],"profit_loss_change"; row["Profit/Losses_change"]})
        
        #need to test this out to figure out what it's doing
        #print(f"profit_loss_change")

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#profit_loss_change = calculate change of all transactions
#profit_loss_average = def average("Change")
#print(average["Change"])
# add this to the csv and write it out??

# Grab the filename from the original path (from Python extra content folder employee_email_solved.py)
#_, filename = os.path.split(filepath)

# Write updated data to csv file 
#csvpath = os.path.join("budget_data_w_change", filename)
#with open(csvpath, "w") as csvfile:
    #ieldnames = ["Date", "Profit/Losses", "Profit/Losses_change"]
    #writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #writer.writeheader()
    #writer.writerows(profit_loss_change)



#The net total amount of "Profit/Losses" over the entire period
#total_amount = sum(FILENAME["Profit/Losses"])



#The greatest increase in profits (date and amount) over the entire period
#greatest_increase = FILENAME["Profit/Losses"].min()

#The greatest decrease in losses (date and amount) over the entire period
#greatest_decrease = FILENAME["Profit/Losses"].min()

#Print to terminal and export to text file with the results
#summary = DataFrame({"Total Months": [month_count], 
# print("---------------------"), 
# "Total": total_amount}, 
# "Average Change": profit_loss_average, 
# "Greatest Increase in Profits": greatest_increase, 
# "Greatest Decrease in profits": greatest_decrease})

#FROM THE DIRECTIONS/EXAMPLE
#Financial Analysis
#----------------------
#Total Months; XX
#Total: $XXXXX
#Average Change: $XXXX.XX
#Greatest Increase in Profits: Mon-Year ($XXXXXX)
#Greatest Decrease in Profits: Mon-Year ($XXXXXX)