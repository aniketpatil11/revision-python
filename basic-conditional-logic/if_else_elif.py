# Take input from user: return the whether the string is less than 5 characters, greater than 5 characters

prompt = "Enter a string:"
user_input = input(prompt)

if len(user_input) < 5: 
    print("The string has less than 5 characters")
elif len(user_input) > 5: 
    print("The string has more than 5 characters")
elif len(user_input) == 5: 
    print("String has exactly 5 characters")