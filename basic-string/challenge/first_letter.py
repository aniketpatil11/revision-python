# Take input as a password and convert the first letter to uppercase

prompt = "Tell me your password:"
user_input = input(prompt)

if (user_input): 
    stripped_input = user_input.strip()
    print(stripped_input[0].upper())
else: 
    print("Please Enter valid input")