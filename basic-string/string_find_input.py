# Take input and find the required substring; display it

prompt = "Please enter a sentence: "
user_input_string = input(prompt)

prompt = "What do you want to find? : "
user_input_character = input(prompt)
if_found = user_input_string.find(user_input_character)
if if_found != -1: 
    print(f"the letter exists in the string at {if_found} index.")
else:
    print("Character can't be found.")

