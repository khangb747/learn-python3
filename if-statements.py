temperature = 29

if temperature > 35:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20: # (20, 30]
    print("It's a nice day")
    print("Done")
elif temperature > 10: #(10,20]
    print("It's a bit cold")
else:
    print("It's cold")