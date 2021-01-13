#correcting homework from pandas to python script
#import the operating systems to use across systems
#import pandas as pd
import os
#need to import csv reader
import csv

#create variable for file path
file_path=os.path.join("Resources","budget_data.csv")

#output path for the txt file
loadout=os.path.join("Analysis","PyBank_Analysis.txt")


#variable dataframe to reade the csv file, and return headers
#data_file_df = pd.read_csv(file_path)
#data_file_df.head()
#csvfile=open(file_path)
#csvreader=csv.reader(csvfile,delimiter=",")

# Will need to make variables for each item to return from the db. 
with open(file_path,newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    #skip the header
    header = next(csvreader)

# Total Number of Months included in the dataset
#month_total_df=data_file_df['Date'].count()
#month_total_df

#initial initial varialbles and set to 0
    #bud_data=[]
    net_total=0
    #date=[]
    months=0
    curr_rev=0
    prev_rev=0
    total_change=0
    rev_change=[]
    mo_change=[]
    increase_index=["",0]
    decrease_index=["",99999999999]
    
    #initiate a for loop to go down rows
    for row in csvreader:
        #calculate the total months
        months=len(list(csv.reader(open(file_path))))-1
        
        #calculate the net total amount of "Profit/Losses"
        net_total=net_total+(int(row[1]))

        
    #Calculate the month to month change
        curr_rev=int(row[1])-prev_rev
        prev_rev=int(row[1])
        mo_change=mo_change+[row[0]]
        
    #Append to list rev.change then calculate sum of total changes over the entire period   
        rev_change.append(curr_rev)
        total_change=total_change+curr_rev
        
    #Calculate total increase using > and an if statement
        if curr_rev>increase_index[1]:
            increase_index[0]=row[0]
            increase_index[1]=curr_rev
        
     #Calculate total increase using > and an if statement
        if curr_rev<decrease_index[1]:
            decrease_index[0]=row[0]
            decrease_index[1]=curr_rev
    #Calculate the average change over the entire period
        change_avg=(total_change-867884)/(months-1)
        
     

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
print(f"Total Months: {months}")
print(f"Total: ${net_total}")
print(f"Average Change:${change_avg:.2f}")
print(f"Greatest Increase in Profits: {increase_index[0]} (${increase_index[1]})")
print(f"Greatest Decrease in Profits: {decrease_index[0]} (${decrease_index[1]})")
#The greatest decrease in losses (date and amount) over the entire period


# Total Months: Integer
# Total: Dollar Amount
# Average Change: Dollar Amount
# Greatest Increase in Profits: Month-Year (Value $)
# Greatest Decrease in Profits: Month-Year (Value $)

# return all values in a print statement. 

#title file for output
write_txt="PyBank_Analysis.txt"
#open file writer
writefile=open(write_txt,mode='w')

#print the analysis to the file
writefile.write("Financial Analysis\n")
writefile.write("------------------------\n")
writefile.write(f"Total Months: {months}\n")
writefile.write(f"Total: ${net_total}\n")
writefile.write(f"Average Change:${change_avg:.2f}\n")
writefile.write(f"Greatest Increase in Profits: {increase_index[0]} (${increase_index[1]})\n")
writefile.write(f"Greatest Decrease in Profits: {decrease_index[1]} (${decrease_index[1]})\n")

#close the writer
writefile.close()

####### rest of panda coding
# Net total amount of "profit/losses" over the entire period
#net_total_df=data_file_df['Profit/Losses'].sum()
#net_total_df
# use the '$' in the print statement to return a dollar value

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#average_change_df=data_file_df['Profit/Losses'].mean()
#average_change_df

#create an empty list to store the values
#change = []
#create variable for list you want to iterate through
#change_mo = data_file_df['Profit/Losses']
# initiate the variables
#prev_mo = 0
#curr_mo = 0

#start a for loop to iterate through the entire list, create a column titled 'change' 
#then create a place for prev_mo to store its value for the next iteration

#for x in range(len(change_mo)):
#    curr_mo=change_mo[x]
#    data_file_df.loc[x, 'Change']=curr_mo-prev_mo
#    prev_mo = curr_mo

#change_df=data_file_df.loc[1:,'Change'].mean()
#change_df

#The greatest increase in profits (date and amount) over the entire period
#increase_df=data_file_df['Change'].max()
#m_filter_df=data_file_df['Change']==increase_df
#max_df = data_file_df.loc[m_filter_df,'Date']
#print(max_df,increase_df)


#The greatest decrease in losses (date and amount) over the entire period
#decrease_df=data_file_df['Change'].min()
#l_filter_df=data_file_df['Change']==decrease_df
#min_df = data_file_df.loc[l_filter_df,'Date']
#print(min_df,decrease_df)


