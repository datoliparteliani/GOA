def longest_word(string_of_words):
    words = string_of_words.split()
    longest = ""
    last_index = -1
    index = 0

    for i in words:
        if len(i) > len(longest) or (len(i) == len(longest) and index > last_index):
            longest = i
            last_index = index
        index += 1
    return longest