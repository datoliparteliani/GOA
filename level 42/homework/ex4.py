def reverse_words(s):
    words_spl = s.split(" ")
    result = words_spl[::-1]
    return " ".join(result)