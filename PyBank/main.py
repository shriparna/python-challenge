# main.py
# This program will cover the challenge for PyBank
# Logic: 
# 1. Read CSV file from resources (Resources/budget_data.csv)
# 2. Create an empty list for date and profit_loss
# 3. Create a variable for records, prev_difference, greatest_increase, greatest_decrease and intitialize them with 0
# 4. Traverse through the file and skip the header row
# 5. Increement the counter of the records and increment sum of profilt_loss
# 6. Check if current_diff is greater than the previous one then store new as the greatest and record the period
# 7. Check if current_diff is lower than the previous one then store new as the lowest and record the period
# 8. After the end of file print the values

import csv

csvfilepath = "Resources/budget_data.csv"
outputpath = "analysis/output.txt"
totalmonths = 0
total = 0
prev_pl = 0
curr_pl = 0
diff = 0
cum_diff = 0
avg_change = 0
greatest_increase = 0
greatest_decrease = 0

with open (csvfilepath, 'r') as pybankfile:
    csvreader = csv.reader (pybankfile, delimiter=',')

    csvheader = next(csvreader) # skip the header

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
print("Financial Analysis")
print(" ")
print("------------------------------")
print(f"Total Months: {totalmonths}")
print(f"Total : {total}")
print(f"Average Change: {avg_change}")
print(f"Greatest Increase in Profits: {gi_period} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {gd_period} (${greatest_decrease})")
