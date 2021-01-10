#import the operating systems to use across systems
import os
# need to import csv reader
import csv

#create variable for file path
file_path=os.path.join("Resources","election_data.csv")

#use csvfile reader
csvfile=open(file_path)
# below is to read if issues reading on windows
# csvfile = open(csvfile, encoding='utf8')

csvreader=csv.reader(csvfile,delimiter=",")

csv_header=next(csvreader)

# Will need to make variable lists for each item to return from the db. 
#voter_id = []
#county_list=[]
candidate=[]
#dup_cand=[]
votes_cast=0
total_votes=[]

with open(file_path,'r'):
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvreader)
    
#For loop using an if statement to total votes for a candidate
#use append to remove duplicates
    for row in csvreader:
        votes_cast=votes_cast+1
        candidate=csvreader[2]
        if candidate in all_candidates:
            cand_index=candidates.index(candidate)
            total_votes[cand_index]=total_votes[cand_index]+1
        else:
            cand_index.append(candidate)
            total_votes.append(1)
            
# The total number of votes cast
 #   votes_cast=len(voter_id)
#print(votes_cast)

# A complete list of candidates who received votes
# remove duplicate values from the candidate list
# start a for loop for csvreader to remove the duplicate candidate values
# use set to remove dulicates
#dup_cand=[]
    for row in csvreader:
        

#create a dict to store the candidates
  #  PyPoll={}

# The total number of votes each candidate won
# Start a for loop through the total_candidates in dup_cand, then get the percentage using round and an equation 
#to get the 
 
 #   for y in range(len(total_candidates)):
 #       PyPoll[candidate[y]]=dup_cand.count(total_candidates[y])
        
        # The percentage of votes each candidate won
#        vote_percent=float(PyPoll(total_candidates[y]) / votes_cast * 100)
        

 #   print (candidate + ": " + str(vote_percent) + "% (" + str(sum_candidates) + ")")
# The winner of the election based on popular vote.


# Header: 
# Election Results
# -------------------------
# Total Votes: Long
# -------------------------
# Candidate 1 : Percentage of Vote : (total votes)
# Candidate 2 : Percentage of Vote : (total votes)
# Candidate 3 : Percentage of Vote : (total votes)
# Candidate 4 : Percentage of Vote : (total votes)
# -------------------------
# Winner: Candidate name
# -------------------------
print("Election Results")
print("-------------------------")
print(f"Total Votes: {votes_cast}")
print("-------------------------")
for votes in range(len(total_candidates)):
    print (f"{candidate} : {vote_percent}% :({total_candidates})")
