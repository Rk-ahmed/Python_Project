#given list of ages
ages : list[int | None] = [22, None, 17, 45, None, 15, 60, 30, 55,None]

#Step1 : Calculate sum and count of valid ages (non-None values)
total = 0
count = 0

for age in ages:
    if age is not None:
        total += age
        count +=1
#Step 2 : Calculate average age
average_age = round((total / count),2)

#Step 3 :Replace with none values with average age
cleaned_ages = []
for age in ages:
    if age is None:
        cleaned_ages.append(average_age)
    else:
        cleaned_ages.append(age)

print(f"Cleaned Ages: {cleaned_ages}")
