# Pritnt strings in thre ways 

# 1. String concatenation

weight = 0.2
animal = "newt"
print( str(weight) + "kg is the weight of the " + animal + ".")

# 2. Using .format() method
print( "{} kg is the weight of the {}".format(weight, animal)) 

# 3. Using string interpolation 

print(f"{weight} kg is the weight of the {animal}")