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

print(result)