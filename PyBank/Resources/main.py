import os
import csv

net_profit_loss = 0
row_count = 0
prev_row = 0
sum_profit = 0
change = 0
avg_chng = 0
greatest_increase = 0
greatest_decrease = 0
increase_month = 0
decrease_month = 0
total_change = 0

csvpath = os.path.join("..","Resources","budget_data.csv")
with open(csvpath, 'r') as f:
    csvreader = csv.reader(f, delimiter = ',')
    next(csvreader, None)  # skip the headers
    
    # loop through each row in the file data
    for row in csvreader:
        curr_row = int(row[1])      
        
        # accumulate the total amount
        net_profit_loss += curr_row
        
        
        # calculate the change in profit/loss month over month as a difference between current month's data from the prev month's
        if row_count > 0:
            change = curr_row - prev_row

        total_change += change   
        prev_row = curr_row
        
        # compute the greatest increase in the profit/loss change
        if change > greatest_increase:
            greatest_increase = change
            increase_month = row[0]
            
        # compute the greatest decrease in the profit/loss change    
        if change < greatest_decrease:
            greatest_decrease = change
            decrease_month = row[0]
            
        # increment the row counter
        row_count +=1

    # Average change computation requires division by 1 less than the number of rows
    avg_chng = round(total_change / (row_count - 1),2)
    
    # Display the properly formatted results on the terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {row_count}")
    print(f"Total: ${net_profit_loss}")
    print(f"Average Change: ${avg_chng}")
    print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")

    # set the path to save the text file and open it in write mode to save the results
    txtpath = os.path.join("..","Resources","budget_results.txt")
    with open(txtpath, 'w') as txtfile:
    
        txtfile.write("Financial Analysis \n")
        txtfile.write("---------------------------- \n")
        txtfile.write(f"Total Months: {row_count} \n")
        txtfile.write(f"Total: ${net_profit_loss} \n")
        txtfile.write(f"Average Change: ${avg_chng} \n")
        txtfile.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase}) \n")
        txtfile.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")
