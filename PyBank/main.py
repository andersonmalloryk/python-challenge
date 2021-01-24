#import os module to create a file path and to read a CSV file
import os
import csv

budget_data = os.path.join('Resources', 'budget_data.csv')

#open file using a dictionary reader
with open(budget_data, newline='') as csvfile:
    input_file = csv.DictReader(csvfile)

    #set variables
    total_amount = 0
    min_change = 0
    max_change = 0
    percent_change = []
    previous = None
    average_change = 0
    month_count = 0

    #set up a for loop to idnetify and set variables
    for row in input_file:
        #if the previous profit/losses is not equal to zero then we can run the equation
        if previous is not None:
            profit_loss_change = (int(row["Profit/Losses"])-previous)
        #if the previous profit/losses is equal to zero the change is also zero
        else:
            profit_loss_change = 0
        #reset the previous number to hold for the equation
        previous = int(row["Profit/Losses"])
        #add the change value to a list 
        percent_change.append(profit_loss_change)
        #set the month count and the total amount with a smiple counter and sum funtion
        month_count += 1
        total_amount += int(row["Profit/Losses"])
        #use if statements to save the largest and smallest change with the appropriate dates
        if profit_loss_change < min_change:
            min_change = profit_loss_change
            min_month = (row["Date"])
        if profit_loss_change > max_change:
            max_change = profit_loss_change
            max_month = (row["Date"])
    #pull average change by summing all the numbers in the change value list and divide it by the number of months that have a change value (85)
    average_change = round(sum(percent_change) / (month_count - 1),2)

#FROM THE DIRECTIONS/EXAMPLE
print("Financial Analysis")
print("----------------------")
print("Total Months: " + str(month_count))
print("Total: $" + str(total_amount))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits:" + max_month + " ($" + str(max_change) + ")")
print("Greatest Decrease in Profits:" + min_month + " ($" + str(min_change) + ")")

#print to txt file with results
f = open(os.path.join('Analysis','results.txt'),'w+')
f.writelines("Financial Analysis\n")
f.writelines("----------------------\n")
f.writelines("Total Months: " + str(month_count)+"\n")
f.writelines("Total: $" + str(total_amount)+"\n")
f.writelines("Average Change: $" + str(average_change)+"\n")
f.writelines("Greatest Increase in Profits:" + max_month + " ($" + str(max_change) + ")"+"\n")
f.writelines("Greatest Decrease in Profits:" + min_month + " ($" + str(min_change) + ")")
f.close()