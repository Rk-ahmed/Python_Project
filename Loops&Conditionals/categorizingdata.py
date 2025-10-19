# Categorizing data
#Given Rooms price 

prices = [25000, 120000, 80000, 50000, 150000, 60000]

for price in prices:
    if price < 50000:
        print(f"Low Prices below: {price}")
    elif price > 50000 and price < 100000:
	    print(f"Medium Prices: {price}")
else:
	    print(f"High Prices: {price}")