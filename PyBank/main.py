import csv 
import os


INPUT_PATH = os.path.join('Resources', 'budget_data.csv')
MONTH_INDEX = 0
PROFIT_INDEX = 1


os.chdir(os.path.dirname(os.path.realpath(__file__)))


def calc_pybank(budgetcsv):
    global total_months
    total_months = 0
    global net_total
    net_total = 0 
    global sum_change
    sum_change = 0
    global count_change
    count_change = 0
    global greatest_inc
    greatest_inc = 0
    global greatest_dec
    greatest_dec = 0
    global date_inc
    date_inc = ""
    global date_dec
    date_dec = ""
    A = True
    prof_change = 0

    for row in budgetcsv:
        total_months += 1
        net_total += int(row[1]) 
        if A:
            month = int(row[1])
            A = False
        else:
            current_month = int(row[1])
            prof_change = current_month - month
            month = current_month 
            sum_change += prof_change
            count_change += 1
        if greatest_inc < prof_change:
            greatest_inc = int(prof_change)
            date_inc = str(row[0])
        if greatest_dec > prof_change:
            greatest_dec = int(prof_change)
            date_dec = str(row[0])
    return (total_months,net_total,sum_change,count_change,greatest_inc,greatest_dec,date_inc,date_dec)

    
with open(INPUT_PATH) as csv_file:
   csv_reader = csv.reader(csv_file) 
   header = next(csv_reader)
   calc_pybank(csv_reader)

print("financial Analysis")
print("---------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${sum_change/count_change:.2f}")
print(f"Greatest Increase in Profits: {date_inc} (${greatest_inc})")
print(f"Greatest Decrease in Profits: {date_dec} (${greatest_dec})")

path_table = os.path.join("analysis", "budgetfile.txt")

with open(path_table, "w") as text_file:
    text_file.write("financial Analysis\n")
    text_file.write("---------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${net_total}\n")
    text_file.write(f"Average Change: ${sum_change/count_change:.2f}\n")
    text_file.write(f"Greatest Increase in Profits: {date_inc} (${greatest_inc})\n")
    text_file.write(f"Greatest Decrease in Profits: {date_dec} (${greatest_dec})\n")



            

