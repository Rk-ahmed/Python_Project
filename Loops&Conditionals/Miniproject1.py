#💼 Mini Project 1 — Transaction Analyzer
''' Task:
Categorize transactions as: “Small” (<500) “Medium” (500–2000) “Large” (>2000)
Count how many are in each category. Print summary. '''

#Given transaction list
transactions = [120, 500, 3000, 50, 600, 10000, 900,1700,2200,4500,3000,2500,700,400,150,800,60,30,200,4000]

Small = 0
Medium = 0
Large = 0

for trans in transactions:
    if trans < 500:
        Small +=1
    elif trans >= 500 and trans <= 2000:
        Medium +=1 
    else:
        Large +=1

print(f"In Small category {Small} exist.")
print(f"In Medium category {Medium} exist.")
print(f"In Large category {Large} exist.")