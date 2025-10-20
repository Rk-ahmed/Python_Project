# 💼 Mini Project 3 — Automation: Backup Monitor
''' Task: For each backup: If size = 0 → print “❌ Failed Backup: filename” Else → print “✅ Successful Backup: filename”
Count how many succeeded and failed. '''

backups = [
    {"filename": "backup_01.zip", "size": 120},
    {"filename": "backup_02.zip", "size": 0},
    {"filename": "backup_03.zip", "size": 150},
    {"filename": "backup_04.zip", "size": 0},
]

succeeded = 0
failed = 0

for back in backups:
    filename = back["filename"]
    size = back["size"]
    
    if size == 0:
        print(f"❌ Failed Backup: {filename}")
        failed +=1
    else:
        print(f"✅ Successful Backup: {filename}")
        succeeded +=1

print("\nSummary:")
print(f"Total Successful Backups: {succeeded}")
print(f"Total Failed Backups: {failed}")