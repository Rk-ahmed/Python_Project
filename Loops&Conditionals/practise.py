# Example 1 – Filter numbers greater than 50
''' numbers : int = [25,40,35,40,67,85,100,95,70]

for num in numbers:
	if num > 50:
	    print(f"Number is greater than 50 : {num}") '''
     
#Example 2 – Count how many numbers are even and odd
''' numbers : int=[1,2,3,4,5,6,7,8,9]
odd_count = 0
even_count = 0 


for num in numbers:
	if num % 2 ==0:
	    even_count += 1
else:
	    odd_count += 1
print(f"Total even numbers: {even_count}")
print(f"Total odd numbers: {odd_count}") '''

# Example 3 – Automatically detect low sales
'''sales = [1200, 300, 900, 1500, 400]
threshold = 800

for s in sales:
    if s > threshold:
        print(f"High sales: {s}")
    else:
        print(f"Low sales: {s}")'''

#🧩 Level 1 — Basic

#Print all numbers from 1 to 20.
'''for num in range(1,20):
    print(num) '''
    
#Print only even numbers between 1 and 20 using a loop and conditionals.
''' for num in range(1,20):12
    if num % 2 ==0:
        print(f"Only Even number: {num}") '''

#Ask the user for a number and print whether it’s positive, negative, or zero.
''' user_input = int(input('Please enter a number: '))

if user_input > 0:
        print(f"Its a positive number : {user_input}")
elif user_input < 0:
        print(f"Its a Negative number : {user_input}")
else:
        print(f"Its a zero : {user_input}") '''

# Level 2 — Intermediate

#Given a list of temperatures [33, 36, 25, 40, 22, 29],
#print “Hot” for temperatures > 35, “Warm” for 25–35, and “Cool” otherwise.

''' temperatures : int=[33,36,25,40,27,29]

for temp in temperatures:
    if temp > 35:
	    print(f"Its a Hot Weather")
    elif temp > 25 and temp < 35:
	    print(f"Its a Warm Weather")
    else:
	    print(f"Its a Cool Weather")  '''
     
#Given a list of marks [87, 45, 66, 92, 51, 38],
#count how many students passed (>= 50) and how many failed.

''' marks = [87, 45, 66, 92, 51, 38]
passed = 0
failed = 0

for mark in marks:
    if mark >= 50:
        passed += 1
    else:
        failed += 1

print(f"All passed students: {passed}")
print(f"All failed students: {failed}") '''

#Suppose you have a list of prices [120, None, 250, None, 400].
#Loop through them — if the price is None, print “Missing Value”, else print the price.

prices = [120,None,250,None,400]

for price in prices:
    if price is None:
        print("Missing Value")
    else:
        print(f"Here is price: {price} ")






