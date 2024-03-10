# Function: to return cube of a number 

def cube_of_n(x):
    return pow(x, 3)


prompt = "Enter a number for which you want to compute the cube:"
x = int(input(prompt))

computed_x = cube_of_n(x)
print(computed_x)