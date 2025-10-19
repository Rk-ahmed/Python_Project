# Find and print all sales that are more than 3 times the average (these are outliers).
#Given sales data
sales = [150, 200, 250, 300, 350, 400, 450, 500, 2300, 2400, 2500, 2600, 2700, 2800,4500]

total = 0
count = 0

for sale in sales:
    total += sale
    count += 1

#calculate average sales
average_sales = round(total / count,2)
print(f"Average Sales: {average_sales}")

#Identify outliers (sales > 3 times average sales)
outliers = []
for sale in sales:
    if sale > 3 * average_sales:
        outliers.append(sale)

print(f"Outlier Sales: {outliers}")


