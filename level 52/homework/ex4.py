def remove_consecutive_duplicates(s : str) -> str:
    words = s.split()
    result = []
    
    for i in range(len(words)):
        if i == 0 or words[i] != words[i - 1]:
            result.append(words[i])
    
    return ' '.join(result)