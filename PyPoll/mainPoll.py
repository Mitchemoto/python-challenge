#import the operating systems to use across systems
import os
# need to import csv reader
import csv

#create variable for file path
file_path=os.path.join("Resources","election_data.csv")

#use csvfile reader
csvfile=open(file_path)
# below is to read if issues since on windows
# csvfile = open(csvfile, encoding='utf8')

csvreader=csv.reader(csvfile)

csv_header=next(csvreader)

# Will need to make variables for each item to return from the db. 

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

# create dictionary to return all values in the following format

# Header: 
# Election Results
# -------------------------
# Total Votes: Long
# -------------------------
# Candidate 1 : Percentage of Vote : (total votes)
# Candidate 1 : Percentage of Vote : (total votes)
# Candidate 1 : Percentage of Vote : (total votes)
# Candidate 1 : Percentage of Vote : (total votes)
# -------------------------
# Winner: Candidate name
# -------------------------