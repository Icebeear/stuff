alphabet = {}
with open("alphabet.txt") as file:
    for line in file:
        alphabet[line.split()[0].lower()] = line.split()[1]
    
text = input("Text to Morse: ")
convert_text = ''
for letter in text:
    try: 
        convert_text += alphabet[letter.lower()] + " "
    except:
        convert_text += "/" + " "
print(convert_text)