text = "i play basketball"
result = []
word = ""

for i in text:  
    if i == " ":  
        result.append(word)  
        word = ""  
    else:  
        word += i  
result.append(word)

joined_text = ""
for i in result:
    if joined_text:
        joined_text += " "
    joined_text += i

print(joined_text)