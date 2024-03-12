# ValueError: if the value is mismatched


try: 
    user_input = int(input("Enter an integer : "))
    print(user_input)
except ValueError: 
    print("Please enter a valid integer")