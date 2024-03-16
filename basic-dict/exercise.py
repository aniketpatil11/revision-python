# Exercise 1: 
captains = {}

# Exercise 2: 
# Using brakcet notation 

captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

# Exercies 3: check words in dictionary

if "Enterprise" not in captains: 
    captains["Enterprise"] = "Unknown"

if "Discovery" not in captains:
    captains["Discovery"] = "Unknown"

# Exercise 4
for ship, captain in captains.items(): 
    print(f"The {ship} is captained by {captain}.")

# Exercise 5
del captains["Discovery"]


# Creating dictionary using dict()

captains = dict([
    ("Enterprise", "Picard"), 
    ("Voyagar", "Janeway"),
    ("Defiant", "Sisko"), 
    ("The Pirates", "Jack")
]) 

for key,value in captains.items():
    print(key, value)