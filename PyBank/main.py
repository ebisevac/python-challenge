import os
import csv


input_path=os.path.join("Resources","budget_data.csv")
with open(input_path,newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv.header=next(csvreader)
    first_row= next(csvreader)
    max_profit=float(first_row[1])
    min_profit=max_profit
    tot_month=1
    tot_amount=max_profit
    max_profit_date= first_row[0]
    min_profit_date=max_profit_date
    for row in csvreader:
         if row[0]!="":
             tot_month+=1
         if row[1] !="":
             tot_amount+= float(row[1])
             if float(row[1])>max_profit:
                 max_profit=float(row[1])
                 max_profit_date=row[0]
             elif float(row[1])<min_profit:
                 min_profit=float(row[1])# # #                 
                 min_profit_date=row[0]
                 

average_changes=int(tot_amount/tot_month)


print(f"""
        Total number of months = {tot_month}, 
        Total Amount = ${tot_amount}, 
        Average Changes = ${average_changes},
        Maximum profit of ${max_profit}, happened on {max_profit_date}, 
        Maximum loss of ${min_profit}, happened on {min_profit_date}""")
