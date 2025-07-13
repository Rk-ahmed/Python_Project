import random

secret_number = random.randint(1,50)
print(f'Secret Number Generate by Python is {secret_number}.')

guess = 0

while guess!=secret_number:
    guess=int(input("Give me your input: "))

    if guess < secret_number:
        print("Too Low")
    elif guess > secret_number:
        print("Too High")
    else:
        print("Correct, You win")