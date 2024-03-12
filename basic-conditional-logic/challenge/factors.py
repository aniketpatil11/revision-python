# Print the factors of N: where N>0

prompt = "Enter a number to find its factors : "
n = int(input(prompt))

for i in range(1,n+1): 
    if (n%i) == 0: 
        print(f"{i} is factor of {n}")



