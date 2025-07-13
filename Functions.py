# #Check the number is odd or even
# def odd_or_even(number):
#     if number % 2 ==0:
#         return('This number is Even')
#     else:
#         return('This number is odd')

# print(odd_or_even(10))



# 3. Vowel Counter
# Use: Loops, string handling, functions
#  What it should do:
# Take a string input

# Count and return the number of vowels

# def count_vowels(text):
#     vowels='aeiouAEIOU'
#     count = 0
#     for char in text:
#         if char in vowels:
#             count += 1
#     return count
    
# print(count_vowels('I am Rakib Ahmed, I want to be a Great Data Scientist'))


# Simple Grading System
# Use: Multiple return values, conditional grading

# What it should do:
# Accept marks (0–100)

# Return grade (A, B, C...) and pass/fail status

def marks(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = "F"

    Status = 'Pass' if score >= 60 else 'Fail'
    return score, Status

g, s = marks(85)

print(f"Grade: {g}, Status: {s}")



















