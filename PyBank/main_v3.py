# PyBank 
#--------------------------------------------------------------------------------------
# [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `profit/losses`
#--------------------------------------------------------------------------------------
 
# Python script that analyzes the records to calculate each of the following:

## Dependencies
import csv

# Files to Load
file_to_load = "C:/Users/boninjv/Desktop/python-challenge/PyBank/Resources/budget_data.csv"
file_to_output = "C:/Users/boninjv/Desktop/python-challenge/PyBank/Resources/budget_analysis.txt"

# Variables to Track
total_months = 0
total_profitlosses = 0
prev_profitlosses = 0
profitlosses_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]
profitlosses_changes = []

# Read Files
with open(file_to_load) as profitlosses_data:
    reader = csv.DictReader(profitlosses_data)

    # Loop through all the rows of data we collect
    for row in reader:

        # Calculate the totals
        total_months = total_months + 1
        total_profitlosses = total_profitlosses + int(row["profitlosses"])
        # print(row)

        # Keep track of changes
        profitlosses_change = int(row["profitlosses"]) - prev_profitlosses
        # print(profitlosses_change)

        # Reset the value of prev_profitlosses to the row I completed my analysis
        prev_profitlosses = int(row["profitlosses"])
        # print(prev_profitlosses)

        # Determine the greatest increase
        if (profitlosses_change > greatest_increase[1]):
            greatest_increase[1] = profitlosses_change
            greatest_increase[0] = row["Date"]

        if (profitlosses_change < greatest_decrease[1]):
            greatest_decrease[1] = profitlosses_change
            greatest_decrease[0] = row["Date"]

        # Add to the profitlosses_changes list
        profitlosses_changes.append(int(row["profitlosses"]))

    # Set the profitlosses average
    profitlosses_avg = sum(profitlosses_changes) / len(profitlosses_changes)
    
    # Show Output
    print()
    print()
    print("-------------------------")
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total : " + "$" + str(total_profitlosses))
    print("Average Change: " + "$" + str(round(sum(profitlosses_changes) / len(profitlosses_changes),2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
    
# Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write("------------------------")
    txt_file.write("Financial Analysis")
    txt_file.write("------------------------")
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total profitlosses: " + "$" + str(total_profitlosses))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(profitlosses_changes) / len(profitlosses_changes),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")


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