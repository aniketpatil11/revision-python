# is the difference between two number a integer

prompt = "Enter a number:"
user_input1 = float(input(prompt))

prompt = "Enter another number"
user_input2 = float(input(prompt))

print(f"Is the difference between two number is an integer: {(user_input1 - user_input2).is_integer()}")

