lines = ["INFO: User login", "ERROR: File missing", "INFO: Backup done", "ERROR: Timeout"]

error_count = 0

for line in lines:
    if "ERROR" in line:
        error_count += 1

print("Total ERROR lines:", error_count)