def solution(text, ending):
    if len(ending) > len(text):
        return False
    
    return text[len(text) - len(ending):] == ending