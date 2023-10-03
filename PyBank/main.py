# import csv module
import csv

#set file path
csvpath = "E:\Data analytics bootcamp\Challenges\module 3\Starter_Code\PyBank\Resources\\budget_data.csv"

#create empty list for profits
total_profit = []

#create var for max&min profit and date of profit
max_value = 0
date_of_max_value = None
min_value = float("inf")
date_of_min_value = None
number = 0

#empty list for months
months = []

# Open the CSV using the UTF-8 encoding
with open(csvpath,encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)

    for row in csvreader:
        #add profit/losses to total_profit list as integers 
        total_profit.append(int(row[1]))
        months.append(row[0])
        
        #find max values
        date = row[0]  
        number = (int(row[1]))  
        #Check if this value is greater than the current maximum 
        if number > max_value:
            max_value = number
            date_of_max_value = date

        # #find min values
        # datemin = row[0]  
        # numbermin = (int(row[1]))  
        # #Check if this value is greater than the current maximum 
        # if numbermin < min_value:
        #     min_value = numbermin
        #     date_of_min_value = datemin


        ##### MIN AND MAX ARE WRONG, FIND MIN AND MAX CHANGE NOT OVERALL MIN AND MAX

    #find amount of months
    total_months= len(months)

    #sum the total profits and store it in total
    total = sum(total_profit)

    #find average change
    change = []
    for i in range(1, len(total_profit)):
        change.append(total_profit[i] - total_profit[i - 1])
    average_change = sum(change) / len(change)
    decimal_places = 2
    average_change = round(float(average_change), decimal_places)

        
# #Print the analysis
# print("Financial Analysis")
# print()
# print("----------------------------")
# print()
# print(f"Total Months: {total_months}")
# print()
# print(f"Total: ${total}")
# print()
# print(f"Average Change: ${average_change}")
# print()
# print(f"Greatest Increase in Profits: {date_of_max_value} (${max_value})")
# print()
# print(f"Greatest Decrease in Profits: {date_of_min_value} (${min_value})")


# output_file = "E:\Data analytics bootcamp\Challenges\module 3\Starter_Code\PyBank\\analysis.txt"

# #Print the analysis to a txt file
# # Open the file in write mode
# with open(output_file, "w") as file:
#     # Redirect the standard output (stdout) to the file
#     import sys
#     sys.stdout = file
    
#     print("Financial Analysis")
#     print()
#     print("----------------------------")
#     print()
#     print(f"Total Months: {total_months}")
#     print()
#     print(f"Total: ${total}")
#     print()
#     print(f"Average Change: ${average_change}")
#     print()
#     print(f"Greatest Increase in Profits: {date_of_max_value} (${max_value})")
#     print()
#     print(f"Greatest Decrease in Profits: {date_of_min_value} (${min_value})")

# # Reset the standard output to the console
# sys.stdout = sys.__stdout__

# # Notify the user that the output has been saved to the file
# print(f"The financial analysis has been saved to '{output_file}'")