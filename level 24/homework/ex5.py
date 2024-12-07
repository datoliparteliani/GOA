words = []

while True:
    word = input("enter any word (or 'done' to finish): ")
    if word == "done":
        break
    words.append(word)

result = " ".join(words)

print(f"these are your words: {result}")