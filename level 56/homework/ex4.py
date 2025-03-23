def vowel_indices(word):
    word = word.lower()
    vowels = "aeiouy"
    arr = []

    for i in range(len(word)):
        if word[i] in vowels:
            arr.append(i + 1)
    return arr