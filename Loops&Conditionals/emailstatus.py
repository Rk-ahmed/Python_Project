#Email Status Checker
emails = ["sent", "failed", "sent", "pending", "failed"]

for email in emails:
    if email == "sent":
        print(f"Email Status: {email} → '✅' ")
    elif email == "failed":
        print(f"Email Status: {email} → '❌' ")
    else:
        print(f"Email Status: {email} → '⚠️' ")
        
        

        