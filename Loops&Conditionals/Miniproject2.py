#💼 Mini Project 2 — Data Quality Checker
''' Task: Check each record:
If name or age is None, print “⚠️ Missing Data Detected”. Otherwise, print “✅ Record OK”. '''

dataset = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": None},
    {"name": "Carol", "age": 31},
    {"name": None, "age": 28},
]

for data in dataset:
    name = data["name"]
    age = data["age"]
    
    if name is None and age is None:
        print("⚠️ Missing Data Detected.")
    else:
        print("✅ Record OK.")