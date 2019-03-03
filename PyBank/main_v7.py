# PyBank 
#--------------------------------------------------------------------------------------
# [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `profit/losses`
#--------------------------------------------------------------------------------------
 
# Python script that analyzes the records to calculate each of the following:

# Dependencies
import csv

# Path to collect data from the Resources folder,adjust appropriately
file_to_load = "C:/Users/boninjv/Desktop/python-challenge/PyBank/Resources/budget_data.csv"
file_to_output = "C:/Users/boninjv/Desktop/python-challenge/PyBank/Resources/budget_analysis.txt"

# Read data from the Resources folder
with open(file_to_load, newline="") as csvfile:
    
 
    # Read header row, print it, set it aside
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
     
       
    # Declare in Memory Variables 
    Months = []
    Profit_Loss = []
    Differences = []
    Greatest_Increase_Date = ""
    Greatest_Decrease_Date = ""
        
    # Loop through the rows of *.csv
    for row in csvreader:
        Months.append(row[0])   
        Profit_Loss.append(int(row[1]))
        
        
    #Show Output
    print(f"-------------------------------")
    print(f"Financial Analysis for Pybank")
    print(f"-------------------------------")
    print(f"Total Months: ", len(Months))
    print(f"Total P&L: $", sum(Profit_Loss))
       
    for i in range(1, len(Profit_Loss)):
        
        # Find average change between months
        Differences.append(Profit_Loss[i] - Profit_Loss[i-1])
        
        # Find average of values
        Average_Change = sum(Differences) / len(Differences)
              
        # Greatest increase in profits (date and amount) over the entire period
        Greatest_Increase = max(Differences)
        Greatest_Increase_Date = str(Months[Differences.index(max(Differences))])

        # Greatest decrease in losses (date and amount) over the entire period
        Greatest_Decrease = min(Differences)
        Greatest_Decrease_Date = str(Months[Differences.index(min(Differences))])
    
     # Print Statements
    print(f"Average Change: $", round(Average_Change,2))  
    print(f"Greatest Increase: ", Greatest_Increase_Date, "($", Greatest_Increase,")")
    print(f"Greatest Decrease: ", Greatest_Decrease_Date, "($", Greatest_Decrease,")")


# Print the analysis to the terminal and export a text file with the results.
with open(file_to_output, "w") as writefile:
    writefile.writelines('------------------------\n')
    writefile.writelines('Financial Analysis for Pybank\n')
    writefile.writelines('------------------------\n')
    writefile.writelines('Total Months: ' + str(len(Months)) + '\n')
    writefile.writelines('Total P&L: $' + str(sum(Profit_Loss)) + '\n')
    writefile.writelines('Average Change: $' + str(round(Average_Change,2)) + '\n')
    writefile.writelines('Greatest Increase: ' + Greatest_Increase_Date + ' ($' + str(Greatest_Increase) + ')'+ '\n')
    writefile.writelines('Greatest Decrease: ' + Greatest_Decrease_Date + ' ($' + str(Greatest_Decrease) + ')')
  
# Template
  #```text
  #Financial Analysis
  #----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: -$2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
  #```month
#'--------------------------------------------------------------------------------------