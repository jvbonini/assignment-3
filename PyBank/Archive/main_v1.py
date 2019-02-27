# PyBank 
#--------------------------------------------------------------------------------------
# [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `profit/losses`
#--------------------------------------------------------------------------------------
 
# Python script that analyzes the records to calculate each of the following:
 
# 0. Creates a variable with a string "Financial Analysis"
title = "Financial Analysis"

# 1. Prints a statement adding the variable
print(title)
print("----------------------------------------")

# 2. Path to collect data from the Resources folder
# Modules
import os
import csv
# Set path for file
csvpath = os.path.join("C:/Users/boninjv/Desktop/python-challenge/PyBank/Resources/budget_data.csv")

# 3. The total number of months included in the dataset
# Variables to Track
total_months = 0
total_profit/losses = 0
prev_profit/losses = 0
profit/losses_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]
profit/losses_changes = []

# Read Files
with open(csvpath) as profit/losses_data:
    reader = csv.DictReader(profit/losses_data)

    # Loop through all the rows of data we collect
    for row in reader:

        # Calculate the totals
        total_months = total_months + 1
        total_profit/losses = total_profit/losses + int(row["profit/losses"])
        # print(row)

        # Keep track of changes
        profit/losses_change = int(row["profit/losses"]) - prev_profit/losses
        # print(profit/losses_change)

        # Reset the value of prev_profit/losses to the row I completed my analysis
        prev_profit/losses = int(row["profit/losses"])
        # print(prev_profit/losses)

        


# The net total amount of "profit/losses" over the entire period
# The average of the changes in "profit/losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#'--------------------------------------------------------------------------------------

# Template
  #```text
  #Financial Analysis
  #----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
  #```month
#'--------------------------------------------------------------------------------------