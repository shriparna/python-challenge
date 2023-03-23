# main.py
# This program will cover the challenge for PyBank
# Logic: 
# Read CSV file from Resources (Resources/budget_data.csv) 
# Create variables totalmonths, total, difference
# Create variables for records, prev_profitloss, current_profitloss, greatest_increase, greatest_decrease and intitialize them with 0
# Create an empty list for output so that it can be printed on the console and written to the output file at the same time
# Traverse through the file and skip the header row
# For the first row note down the profit_loss as previous profit_loss
# Increment the counter of the records in totalmonths and increment sum of profilt_loss in total
# Calculate difference by subtracting previous profit_loss from current profil_loss and this difference to cumulative difference
# Check if current_diff is greater than the previous one then store new as the greatest and record the period
# Check if current_diff is lower than the previous one then store new as the lowest and record the period
# Assign current profit_loss to previous profit_loss
# After the end of input file 
# Append the analysis details to the output text
# Open the output file as CSV in anaysis/financial_analysis.csv
# From the output list print the output values on the console and print the details in the output file
import csv

csvfilepath = "Resources/budget_data.csv"
outputfilepath = "analysis/financial_analysis.csv"
totalmonths = 0
total = 0
prev_pl = 0
curr_pl = 0
diff = 0
cum_diff = 0
avg_change = 0
greatest_increase = 0
greatest_decrease = 0
outputtext = []

with open (csvfilepath, 'r') as pybankfile:
    csvreader = csv.reader (pybankfile, delimiter=',')

    csvheader = next(csvreader) # skip the header row

    # append the header row to the outputtext
    outputtext.append("Financial Analysis")
    outputtext.append("------------------------------")

    for row in csvreader:
        totalmonths = totalmonths + 1 
        if totalmonths == 1:
            prev_pl = int(row[1])
        curr_pl = int(row[1])
        total = total + curr_pl
        diff = curr_pl - prev_pl
        if diff > greatest_increase:
            greatest_increase = diff
            gi_period = row[0]
        elif diff < greatest_decrease:
            greatest_decrease = diff
            gd_period = row[0]
        cum_diff = cum_diff + diff
        prev_pl = curr_pl
      
avg_change = round(cum_diff / (totalmonths - 1), 2) # since it start from row 2, we subtract the count by 1  
# append the calculations to the ouptuttext   
outputtext.append(f"Total Months: {totalmonths}")
outputtext.append(f"Total : {total}")
outputtext.append(f"Average Change: {avg_change}")
outputtext.append(f"Greatest Increase in Profits: {gi_period} (${greatest_increase})")
outputtext.append(f"Greatest Decrease in Profits: {gd_period} (${greatest_decrease})")

# print values to a CSV file and the console
with open (outputfilepath, 'w') as csvoutputfile:
    #Initialize the csv.writer
    csvoutput = csv.writer(csvoutputfile)

    #There is no specific header as the output is more like a text format
    for line in outputtext:
        print(line)
        csvoutput.writerow([line])
        