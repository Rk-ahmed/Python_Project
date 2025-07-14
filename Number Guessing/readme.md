## Project: Number Guessing Game

User tries to guess a number randomly chosen by the computer until they get it right.

# Step-by-Step Breakdown
		✅ Step 1: Import Required Library

# Use the random module to generate a random number.
		✅ Step 2: Generate a Random Number

Generate a number between 1 and 100 (or any range you choose).

# Store it in a variable called secret_number.
		secret_number = random.randint(1, 50)
		✅ Step 3: Ask User for a Guess

Use input() to get user input.

# Convert it into an integer using int().
		✅ Step 4: Use a Loop to Keep Asking

# Use a while loop that continues until the user guesses correctly.
		✅ Step 5: Use Conditional Statements

If the user's guess is less than the secret number → print "Too low!"

If it's greater than the secret number → print "Too high!"

If it's equal → print "Correct!, You Win" and exit loop.


# Concepts Practiced

	variables
	
	input()
	
	while loop
	
	if-elif-else conditionals
	
	random.randint()
	
	Type conversion with int()
