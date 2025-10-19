# Given list of temperatures in Celsius
temps_c = [20, 25, 30, 35, 40]

# Empty list to store Fahrenheit values
temps_f = []

# Loop through each Celsius temperature
for temp in temps_c:
    f = (temp * 9/5) + 32
    temps_f.append(round(f, 2))
    
    # Conditional check
    if f > 90:
        print(f"{f}°F → Hot")
    else:
        print(f"{f}°F → Normal")

# Print final Fahrenheit list
print(f"\nAll temperatures in Fahrenheit: {temps_f}")
