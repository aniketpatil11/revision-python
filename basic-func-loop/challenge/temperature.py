# Temperature.py Conversion of temperatures from fahrenheit to Celsius

def convert_cel_to_fah(celsius): 
    f = (celsius * (9 / 5)) + 32
    return f

def convert_far_to_cel(fahrenheit):
    c = (fahrenheit - 32) * 5 / 9
    return c

prompt_c = "Enter a temperature in Celsius C:"
celsius = float(input(prompt_c))

prompt_f = "Enter a temperature in Celsius F:"
fahrenheit = float(input(prompt_f))

conv_c = convert_cel_to_fah(celsius)
conv_f = convert_far_to_cel(fahrenheit)

print(f"Conversion of Celsius to Fahrenheit: {conv_c}")
print(f"Conversion of Fahrenheit to Celsius: {conv_f}")

