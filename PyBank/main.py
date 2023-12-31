# Import csv module
import csv
from pathlib import Path

# Set file path
csvpath = Path(__file__) /"..\Recources\\budget_data.csv"

# Create empty list for profits
total_profit = []

# Create var for max&min change and date of change
max_value = 0
prev_max_value = 0
date_of_max_value = None
min_value = 0
prev_min_value = 0
date_of_min_value = None
number = 0

# Create empty list for months
months = []

# Open the CSV using the UTF-8 encoding
with open(csvpath,encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)

    for row in csvreader:
        # Add profit/losses to total_profit list as integers 
        total_profit.append(int(row[1]))
        months.append(row[0])
        
        # Find max&min values
        date = row[0]  
        number = (int(row[1])) - (int(prev_max_value))
        # Check if this value is greater than the current maximum 
        if number > max_value:
            max_value = number
            date_of_max_value = date
        prev_max_value = row[1]  
        # Check if this value is less than the current minimum 
        if number < min_value:
            min_value = number
            date_of_min_value = date
        prev_min_value = row[1]
     
    # Find amount of months
    total_months= len(months)

    # Sum the total profits and store it in total
    total = sum(total_profit)

    # Find average change
    change = []
    for i in range(1, len(total_profit)):
        change.append(total_profit[i] - total_profit[i - 1])
    average_change = sum(change) / len(change)
    decimal_places = 2
    average_change = round(float(average_change), decimal_places)

        
# Print the analysis
print("Financial Analysis")
print()
print("----------------------------")
print()
print(f"Total Months: {total_months}")
print()
print(f"Total: ${total}")
print()
print(f"Average Change: ${average_change}")
print()
print(f"Greatest Increase in Profits: {date_of_max_value} (${max_value})")
print()
print(f"Greatest Decrease in Profits: {date_of_min_value} (${min_value})")


output_file = Path(__file__) /"..\\analysis.txt"

# Print the analysis to a txt file
# Open the file in write mode
with open(output_file, "w") as file:
    # Redirect the standard output (stdout) to the file
    import sys
    sys.stdout = file
    
    print("Financial Analysis")
    print()
    print("----------------------------")
    print()
    print(f"Total Months: {total_months}")
    print()
    print(f"Total: ${total}")
    print()
    print(f"Average Change: ${average_change}")
    print()
    print(f"Greatest Increase in Profits: {date_of_max_value} (${max_value})")
    print()
    print(f"Greatest Decrease in Profits: {date_of_min_value} (${min_value})")

# Reset the standard output to the console
sys.stdout = sys.__stdout__

# Notify the user that the output has been saved to the file
print(f"The financial analysis has been saved to '{output_file}'")