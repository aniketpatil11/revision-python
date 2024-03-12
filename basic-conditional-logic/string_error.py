# Try - except blocks.ValueError and IndexError 

def string_index_return(string_n, index_n): 
    try:
        index_in_string = int(index_n) 
        return string_n[index_n]
    except ValueError: 
        print("Please enter valid string")
    except IndexError: 
        print("Error: Index is out of bounds for the given string")

user_string = input("Enter a string : ")
user_integer = input("Enter a string at index : ")
returned_char = string_index_return(user_string, user_integer)
print(returned_char)