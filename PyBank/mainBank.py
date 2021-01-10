#import the operating systems to use across systems
import pandas as pd
# need to import csv reader
# import csv

#create variable for file path
file_path="Resources/budget_data.csv"

#variable dataframe to reade the csv file, and return headers
data_file_df = pd.read_csv(file_path)
data_file_df.head()


# Will need to make variables for each item to return from the db. 

# Total Number of Months included in the dataset
month_total_df=data_file_df['Date'].count()
month_total_df

# Net total amount of "profit/losses" over the entire period
net_total_df=data_file_df['Profit/Losses'].sum()
net_total_df
# use the '$' in the print statement to return a dollar value

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#average_change_df=data_file_df['Profit/Losses'].mean()
#average_change_df

#create an empty list to store the values
#change = []
#create variable for list you want to iterate through
change_mo = data_file_df['Profit/Losses']
# initiate the variables
prev_mo = 0
curr_mo = 0

#start a for loop to iterate through the entire list, create a column titled 'change' 
#then create a place for prev_mo to store its value for the next iteration

for x in range(len(change_mo)):
    curr_mo=change_mo[x]
    data_file_df.loc[x, 'Change']=curr_mo-prev_mo
    prev_mo = curr_mo

change_df=data_file_df.loc[1:,'Change'].mean()
change_df

#The greatest increase in profits (date and amount) over the entire period
increase_df=data_file_df['Change'].max()
m_filter_df=data_file_df['Change']==increase_df
max_df = data_file_df.loc[m_filter_df,'Date']
#print(max_df,increase_df)


#The greatest decrease in losses (date and amount) over the entire period
decrease_df=data_file_df['Change'].min()
l_filter_df=data_file_df['Change']==decrease_df
min_df = data_file_df.loc[l_filter_df,'Date']
#print(min_df,decrease_df)


#Formatting 
# Total Months: Integer
# Total: Dollar Amount
# Average Change: Dollar Amount
# Greatest Increase in Profits: Month-Year (Value $)
# Greatest Decrease in Profits: Month-Year (Value $)

# return all values in a print statement. 
# "financial_analysis = 
print("Financial Analysis")
print( "------------------------")
print(f"Total Months: {month_total_df}")
print(f"Total: ${net_total_df}")
print(f"Average Change: ${change_df}"  )
print(f"Greatest Increase in Profits: {max_df} (${increase_df})")
print(f"Greatest Decrease in Profits: {min_df} (${decrease_df})")
#The greatest decrease in losses (date and amount) over the entire period


# Total Months: Integer
# Total: Dollar Amount
# Average Change: Dollar Amount
# Greatest Increase in Profits: Month-Year (Value $)
# Greatest Decrease in Profits: Month-Year (Value $)

# return all values in a print statement. 

