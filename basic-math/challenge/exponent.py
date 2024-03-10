# Take user input: base and exponent and print their result

prompt1 = "Enter a Base:"
base = float(input(prompt1))
prompt2 = "Enter a exponent:"
exponent = float(input(prompt2))
power = base ** exponent

print(f"{base} to the power of {exponent} = {power}")