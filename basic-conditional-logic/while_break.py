# While loop : quit if user input Q or q
prompt = "Enter a character or string, press Q/q to quit:"
user_input = input(prompt)
while ((user_input != 'Q') or (user_input != 'q')):
    prompt = "Enter a character or string, press Q/q to quit: "
    user_input = input(prompt)
    if (user_input == 'Q') or (user_input == 'q'):
        break
