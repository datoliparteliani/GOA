def remove_duplicate_words(s):
    s = s.split(" ")
    no_repeat = []
    for i in s:
        if i not in no_repeat:
            no_repeat.append(i)
    return " ".join(no_repeat)