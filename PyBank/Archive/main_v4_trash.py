# PyBank 
#--------------------------------------------------------------------------------------
# [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `profit/losses`
#--------------------------------------------------------------------------------------
 
# Python script that analyzes the records to calculate each of the following:

# Dependencies
import csv

# Path to collect data from the Resources folder
file_to_load = "C:/Users/boninjv/Desktop/python-challenge/PyBank/Resources/budget_data.csv"
file_to_output = "C:/Users/boninjv/Desktop/python-challenge/PyBank/Resources/budget_analysis.txt"

# Declare in Memory Variables 
total_months = 0
total_profitlosses = 0

prev_profitlosses = 0
profitlosses_change = 0

greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

profitlosses_changes = []

# Get data from the Resources folder
with open(file_to_load) as profitlosses_data:
    reader = csv.DictReader(profitlosses_data)

    # Loop through the rows of *.csv
    for row in reader:

        # Calculate total number of months included in the dataset
        total_months = total_months + 1

        #The net total amount of P&L over the entire period
        total_profitlosses = total_profitlosses + int(row["profitlosses"])
        
        # Record changes
        profitlosses_change = int(row["profitlosses"]) - prev_profitlosses
        
        # Reset the value of prev_profitlosses to the row 
        prev_profitlosses = int(row["profitlosses"])
        
        # Greatest increase in profits (date and amount) over the entire period
        if (profitlosses_change > greatest_increase[1]):
            greatest_increase[1] = profitlosses_change
            greatest_increase[0] = row["Date"]

        # Greatest decrease in losses (date and amount) over the entire period
        if (profitlosses_change < greatest_decrease[1]):
            greatest_decrease[1] = profitlosses_change
            greatest_decrease[0] = row["Date"]

        # Add the value in the profitlosses_changes list
        profitlosses_changes.append(int(row["profitlosses"]))
     
    
    # The average of profitlosses_changes list
        profitlosses_avg = sum(profitlosses_changes) / len(profitlosses_changes)
    
    # Show Output
    print()
    print()
    print("-------------------------")
    print("Financial Analysis for Pybank")
    print("-------------------------")
    print("Total Number of Months: " + str(total_months))
    print("Total P&L : " + "$" + str(total_profitlosses))
    print("Average Change: " + "$" + str(profitlosses_avg))
    print("Greatest Increase in P&L: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease in P&L: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
    
# Print the analysis to the terminal and export a text file with the results.
with open(file_to_output, "w") as txt_file:
    txt_file.write("------------------------")
    txt_file.write("Financial Analysis for Pybank")
    txt_file.write("------------------------")
    txt_file.write("Total Number of Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total P&L: " + "$" + str(total_profitlosses))
    txt_file.write("\n")
    txt_file.write("Average Change1: " + "$" + str(profitlosses_avg))
    txt_file.write("\n")
    txt_file.write("Greatest Increase in P&L: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease in P&L: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")

  
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