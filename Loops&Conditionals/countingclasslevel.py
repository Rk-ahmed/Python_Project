#Counting Class Level
predictions = ["spam", "ham", "ham", "spam", "spam", "ham"]

count_spam = 0
count_ham = 0

for pred in predictions:
    if pred == "spam":
        count_spam += 1
    elif pred == "ham":
        count_ham += 1

print(f"Total spam predictions: {count_spam}")
print(f"Total ham predictions: {count_ham}")