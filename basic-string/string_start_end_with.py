# Review .startwith() and .endwith()

string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEutiful"

print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))


# Now altering strings so that they can print "true"
# for every string

print(string1.lower().startswith("be"))
print(string2.lower().startswith("be"))
print(string3.lower().startswith("be"))
print(string1.lstrip().lower().startswith("be"))


