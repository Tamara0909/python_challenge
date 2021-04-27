line_count= 0
votes = {}
with open("election_data.csv") as file:
    next (file)
    for line in file:
        line_count = line_count + 1
        line = line.strip()
        row = line.split(',')
        candidate = row [2]
        if candidate not in votes.keys() : 
            votes [candidate] = 1 
        else : 
            votes [candidate] = votes [candidate] + 1
largest_votes = 0
largest_votes_candidate = ""
for candidate in votes.keys ():
    print (candidate,votes [candidate]/line_count*100,votes[candidate])
    if votes [candidate] > largest_votes: 
        largest_votes = votes [candidate]
        largest_votes_candidate = candidate
print (largest_votes_candidate)