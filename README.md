# Module 3: python-challenge

## Author: Shridhar Kamat.
<hr>

### Details of the program or pseudo logic
#### Shridhar Kamat
#### Date: 3/23/2023
<hr>
Package Contents:

1. PyBank

    a. [main.py](https://github.com/shriparna/python-challenge/blob/main/PyBank/main.py)

    b. [budget_data.csv](https://github.com/shriparna/python-challenge/blob/main/PyBank/Resources/budget_data.csv)  (Input File)

    c. [financial_analysis.csv](https://github.com/shriparna/python-challenge/blob/main/PyBank/analysis/financial_analysis.csv)   (Output File)
    
2. PyPoll

    a. [main.py](https://github.com/shriparna/python-challenge/blob/main/PyPoll/main.py)

    b. [election_data.csv](https://github.com/shriparna/python-challenge/blob/main/PyPoll/Resources/election_data.csv)    (Input File)    
    [Note: File is too large so Github may not show it]

    c. [election_results.csv](https://github.com/shriparna/python-challenge/blob/main/PyPoll/analysis/election_results.csv)  (Output File)

3. [README.md](https://github.com/shriparna/python-challenge/blob/main/README.md) 

<hr>

## Pseudo Logic  
<hr>

## 1. PyBank

Logic: 
-  Read CSV file from Resources (Resources/budget_data.csv) 
- Create variables totalmonths, total, difference
- Create variables for records, prev_profitloss, current_profitloss, greatest_increase, greatest_decrease and intitialize them with 0
- Create an empty list for output so that it can be printed on the console and written to the output file at the same time
- Traverse through the file and skip the header row
- For the first row note down the profit_loss as previous profit_loss
- Increment the counter of the records in totalmonths and increment sum of profilt_loss in total
- Calculate difference by subtracting previous profit_loss from current profil_loss and this difference to cumulative difference
- Check if current_diff is greater than the previous one then store new as the greatest and record the period
- Check if current_diff is lower than the previous one then store new as the lowest and record the period
- Assign current profit_loss to previous profit_loss
- After the end of input file 
- Append the analysis details to the output text
- Open the output file as CSV in anaysis/financial_analysis.csv
- From the output list print the output values on the console and print the details in the output file
<hr>

## 2. PyPoll

Logic: 
-  Read CSV file from Resources (Resources/election_data.csv).
- Create variable totalvotes and space as candidate
- Create an empty dictionary as we don't know how many candidates and also they may not be in the sorted order
- Create an empty list for output so that it can be printed on the console and written to the output file at the same time
- Traverse through the file and skip the header row
- Increement the counter of the votes in totalvotes
- Check if current candidate from file is not equal to candidate variable then make candidate variable from the candidate file and if the candidate not in dictionary then add the candidate and reset its value to zero
- while the candidate is same as candidate from file increment that candidate's count
- After the end of file 
- Append the candiate details from the dictionary
- Append the winner from the dictionary based on maximum votes
- Open the output file as CSV in anaysis/election_results.csv
- Print the values on the console
- Print the details in the output file
