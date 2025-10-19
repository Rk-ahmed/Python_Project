# Automation Focused practise

files = ["report1.csv", "data_backup.zip", "sales.xlsx", "error.log", "report2.csv"]

for file in files:
    if file.endswith(".csv"):
        print(f"{file} -- Data File Detected")
    else:
        print(f"{file} -- Non Data File")