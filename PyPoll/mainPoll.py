#import the operating systems to use across systems
import os
# need to import csv reader
import csv

# Initiate Variables
#voter_id = []
#county_list=[]
all_candidates=[]
votes_cast=0
total_votes=[]

#create variable for file path
file_path=os.path.join("Resources","election_data.csv")

#use csvfile reader
csvfile=open(file_path)
# below is to read if issues reading on windows
# csvfile = open(csvfile, encoding='utf8')

csvreader=csv.reader(csvfile,delimiter=",")

with open(file_path,newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    #skip the header with next
    column=next(csvreader,"None")
    
#For loop using an if statement to total votes for a candidate
#use append to create a new location to store the candidate values
    for column in csvreader:
        #total votes
        votes_cast=votes_cast+1
        #cadidate the votes are associated with
        candidate=column[2]
        #if statement for for votes assicated with cadidate
        if candidate in all_candidates:
            cand_index=all_candidates.index(candidate)
            total_votes[cand_index]=total_votes[cand_index]+1
        else:
            all_candidates.append(candidate)
            total_votes.append(1)
            
# The total number of votes cast
 #   votes_cast=len(voter_id)
#print(votes_cast)
print("Election Results")
print("-------------------------")
print(f"Total Votes: {votes_cast}")
print("-------------------------")

#initiate variables for next round
percentage_index=[]
most_votes=total_votes[0]
winner_index=0
# A complete list of candidates who received votes
# remove duplicate values from the candidate list
# start a for loop for csvreader with an if/else staement to get the percentage of vote
# as well as the winner

for votes in range(len(all_candidates)):
    vote_percent=total_votes[votes]/votes_cast*100
    percentage_index.append(vote_percent)
    if total_votes[votes] > most_votes:
        most_votes=total_votes[votes]
        print(most_votes)
        winner_index=votes
winner=all_candidates[winner_index]

#print the cadidates, vote percentage, total votes and the winner
for votes in range(len(all_candidates)):
    print (f"{all_candidates[votes]}:{percentage_index[votes]:.3f}%:({total_votes[votes]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")       
#create a dict to store the candidates
#  PyPoll={}

# The total number of votes each candidate won
# Start a for loop through the total_candidates in dup_cand, then get the percentage using round and an equation 
#to get the 
 
 #   for y in range(len(total_candidates)):
 #       PyPoll[candidate[y]]=dup_cand.count(total_candidates[y])
        
        # The percentage of votes each candidate won
#        vote_percent=float(PyPoll(total_candidates[y]) / votes_cast * 100)
        
# print (candidate + ": " + (vote_percent) + "% (" + (sum_candidates) + ")")
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
#print("Election Results")
#print("-------------------------")
#print(f"Total Votes: {votes_cast}")
#print("-------------------------")
#for votes in range(len(all_candidates)):
#    print (f"{candidate[votes]} : {vote_percent[votes]}% :({all_candidates[votes]})")
#print("-------------------------")
#print(f"Winner: {winner}")
#print("-------------------------")

#title file for output
write_file="PyPoll_Results.txt"
#open file writer
writefile=open(write_file,mode='w')

#print the analysis to the file
writefile.write("Election Results\n")
writefile.write("-------------------------\n")
writefile.write(f"Total Votes: {votes_cast}\n")
writefile.write("-------------------------\n")
for votes in range(len(all_candidates)):
    writefile.write(f"{all_candidates[votes]}:{percentage_index[votes]:.3f}%:({total_votes[votes]})\n")
writefile.write("-------------------------\n")
writefile.write(f"Winner: {winner}\n")
writefile.write("-------------------------\n")

#close the writer
writefile.close()

