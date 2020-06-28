import os
import csv

num_votes = [0,0,0,0]
total_votes = 0
unique_list = []

# Define the file path and read it line by line
csvpath = os.path.join("..","Resources","election_data.csv")

with open(csvpath,"r") as f:
   
    next(f)
    freader = csv.reader(f, delimiter = ",")
    
    # For each row determine whether the candidate name is already on a unique list,
    # if not, add the name to the unique list. Also, when the candidate from unique list is found
    # then aggregate the number of votes
    for row in freader:
        candidate_name = row[2]
        if candidate_name not in unique_list:
            unique_list.append(candidate_name)
        for i in range(len(unique_list)):
            if unique_list[i] == candidate_name:
                num_votes[i] += 1
        total_votes += 1
   
    # Display the formatted results on the terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for i in range(len(unique_list)):
        print(f"{unique_list[i]}: {(num_votes[i]/total_votes):.3%} ({num_votes[i]})")
        if num_votes[i] == max(num_votes):
            winner = unique_list[i]
            
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

# store the results in a text file
txtpath = os.path.join("..","Resources","election_results.txt")

with open(txtpath, 'w') as txtfile:

    txtfile.write("Election Results \n")
    txtfile.write("------------------------- \n")
    txtfile.write(f"Total Votes: {total_votes} \n")
    txtfile.write("------------------------- \n")
    for i in range(len(unique_list)):
        txtfile.write(f"{unique_list[i]}: {(num_votes[i]/total_votes):.3%} ({num_votes[i]}) \n")
        
    txtfile.write("------------------------- \n")
    txtfile.write(f"Winner: {winner} \n")
    txtfile.write("-------------------------")
