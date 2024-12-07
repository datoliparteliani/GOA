text = "i love programming, programming is fun"
old_substring = "programming"
new_substring = "coding"

result = ""
i = 0

while i < len(text):
    match = True
    
    for k in range(len(old_substring)):
        if i + k >= len(text) or text[i + k] != old_substring[k]:
            match = False
    
    if match:
        result += new_substring
        i += len(old_substring)
    else:
        result += text[i]
        i += 1

print(result)