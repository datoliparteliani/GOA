def count_letters_and_digits(s):
    count = 0
    
    for i in s.lower():
        if i.isdigit():
            count += 1
        elif i.isalpha():
            count += 1
    return count