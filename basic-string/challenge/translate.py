# convert user input text into "leetspeak" : 
# a -> 4, b = 8, e = 3, l = 1, o = 0, s = 5, t = 7

prompt = "Enter some text:" 
user_input = input(prompt)

text_translate = user_input.replace('a', '4')
text_translate = text_translate.replace('b', '8')
text_translate = text_translate.replace('e', '3')
text_translate = text_translate.replace('l', '1')
text_translate = text_translate.replace('o', '0')
text_translate = text_translate.replace('s', '5')
text_translate = text_translate.replace('t', '7')

print(text_translate)