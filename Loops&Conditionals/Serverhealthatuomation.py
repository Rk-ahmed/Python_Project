#Server Health Automation

servers = {"Server1": 85, "Server2": 45, "Server3": 95, "Server4": 60}

for server, cpu_usage in servers.items():
    if cpu_usage > 90:
        status = "Critical"
    elif 70 <= cpu_usage <= 90:
        status = "Warning"
    else:
        status = "Normal"
    
    print(f"{server}: CPU Usage = {cpu_usage}%, Status = {status}")