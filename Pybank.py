line_count= 0
total = 0
average_change = 0
previous_profit = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0 
greatest_decrease_date = ""
with open("budget_data.csv") as file:
    next (file)
    for line in file:
        line_count = line_count + 1
        line = line.strip()
        row = line.split(',')
        profit = float(row[1])
        if line_count > 1:
            change = profit - previous_profit
            average_change = average_change + change 
            if change > greatest_increase : 
                greatest_increase = change 
                greatest_increase_date = row [0]  
            if change < greatest_decrease :
                greatest_decrease = change 
                greatest_decrease_date = row [0]
        total = total + profit
        previous_profit = profit

print (line_count) 
average_change = average_change /(line_count - 1)
print (total)
print (average_change)
print (greatest_increase_date, greatest_increase)
print (greatest_decrease_date, greatest_decrease)