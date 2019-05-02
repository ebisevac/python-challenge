import os
import csv

cnt=1
candidate={}
input_path=os.path.join("Resources","election_data.csv")
with open(input_path,newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv.header=next(csvreader)
    first_row= next(csvreader)
    candidate[first_row[2]]=1  
    for row in csvreader:
        cnt+=1
        if row[2] not in candidate:
              candidate[row[2]]=1
        else:
              candidate[row[2]] += 1


print(f" Total number of vote {cnt}")

winner=""
largest=0
for names in candidate:
      print(f"{names}: {round(candidate[names]/cnt*100,3)}% ({candidate[names]})")
      if candidate[names]>largest:
          largest=candidate[names]
          winner=names


print(f"Winner: {winner}")


