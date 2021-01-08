#import the operating systems to use across systems
import os
# need to import csv reader
import csv

#create variable for file path
file_path=os.path.join("Resources","budget_data.csv")

#use csvfile reader
csvfile=open(file_path)
# below is to read if issues since on windows
# csvfile = open(csvfile, encoding='utf8')

csvreader=csv.reader(csvfile)

csv_header=next(csvreader)

# Print statment for header 
# "financial_analysis = print(
# "Financial Analysis")
# Print( 
# "------------------------")"

# Will need to make variables for each item to return from the db. 
# Total Number of Months included in the dataset

# Net total amount of "profit/losses" over the entire period

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period

# create dictionary to return all values in the following format
# Total Months: Integer
# Total: Dollar Amount
# Average Change: Dollar Amount
# Greatest Increase in Profits: Month-Year (Value $)
# Greatest Decrease in Profits: Month-Year (Value $)

# return all values in a print statement. 

