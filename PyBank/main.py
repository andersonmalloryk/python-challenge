#import os module to create a file path and to read a CSV file
import os
import csv
#do I need to import string

budget_data = os.path.join('Resources', 'budget_data.csv')

#add a container for the change column to be added to calculate average change of profit and losses
#data = {"Month":[],"Profit":[],"Change"=[]}
change_list= []
profit_loss_change = []

#one idea I have is to set variable of the previous value
    #define a function that is like this:
# def change(r):
#   if(r > 0):
#     result = (r - r-1) / r-1
#       change_list.amend(result)
#   else:
#     result = 0
#   return result
#       change_list.amend(result)


#myList = [row[1]]
#myList.append(equation that doesn't work....)

with open(budget_data, 'r') as csvfile:
     # CSV reader specifies delimiter and variable that holds contents
     budget_reader = csv.reader(csvfile, delimiter=',')

     # Read the header row first 
     next(budget_reader)

     #The total number of months included in the dataset
     month_count = len(list(budget_reader))
     print(month_count)  

     for index, row in enumerate(budget_reader):
        if (index+1 < len(month_count) and index-1 >=0):
            if row[1] == 0:
                profit_loss_change = 0
                change_list.append(float(profit_loss_change))
            else: #row[1] is not None:
                #profit_loss_change = ((row[1]-str(budget_reader[index-1])/str(budget_reader[index-1])
                profit_loss_change = ((row[1]-(budget_reader[row-1])/(budget_reader[row-1])))
                change_list.append(float(profit_loss_change))

print(profit_loss_change)
print(change_list)

# with open(budget_data, 'w', newline='') as csvfile:
#     fieldnames=['Date','Profit/Losses','change']
#     # CSV reader specifies delimiter and variable that holds contents
#     budget_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #for index, row in enumerate(budget_reader):

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#profit_loss_change = calculate change of all transactions
#profit_loss_average = def average("Change")
#print(average["Change"])

# Grab the filename from the original path (from Python extra content folder employee_email_solved.py)
#_, filename = os.path.split(filepath)

# Write updated data to csv file 
#csvpath = os.path.join("budget_data_w_change", filename)
#with open(csvpath, "w") as csvfile:
    #ieldnames = ["Date", "Profit/Losses", "Profit/Losses_change"]
    #writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #writer.writeheader()
    #writer.writerows(profit_loss_change)

    # for row in budget_reader:
    #     if previous is not None or (previous == 0):
    #         profit_loss_change = 0
    #         all_data.append({"month": row["Date"],"profit_loss": row:["Profit/Losses"],"profit_loss_change"; row["Profit/Losses_change"]})
    #     else 
    #         profit_loss_change = ((row[1]-previous)/previous)
    #         all_data.apend({"month": row["Date"],"profit_loss": row:["Profit/Losses"],"profit_loss_change"; row["Profit/Losses_change"]})

    #     previous = row[1]

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

#methodology
#first I need to read the csv file / import the os and csv 
#then I need to count how many months -- simple lenght should work (use from pypoll)
#calculate the total amount of interactions - some kind of sum fumnction of the [2] column
#calculate the change - I think there is a percent change function
    #store the last value and then set up an equation with the current value and print it out to the csv?
#store change in a dictionary with the month column
#report out the max in this change dicationary
#report out the min in this change dictionary
#pull the average from this change dictionary