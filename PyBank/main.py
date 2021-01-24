#import os module to create a file path and to read a CSV file
import os
import csv

budget_data = os.path.join('Resources', 'budget_data.csv')

with open(budget_data, newline='') as csvfile:
    input_file = csv.DictReader(csvfile)

    total_amount = 0
    min_change = 0
    max_change = 0
    percent_change = []
    previous = None
    average_change = 0
    month_count = 0

    for row in input_file:
        if previous is not None:
            profit_loss_change = (float(row["Profit/Losses"])-previous)
        else:
            profit_loss_change = 0
        previous = float(row["Profit/Losses"])
        percent_change.append(profit_loss_change)
        month_count += 1
        total_amount += int(row["Profit/Losses"])
        if profit_loss_change < min_change:
            min_change = profit_loss_change
            min_month = (row["Date"])
        if profit_loss_change > max_change:
            max_change = profit_loss_change
            max_month = (row["Date"])
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

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)