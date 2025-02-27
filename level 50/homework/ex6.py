def open_or_senior(data):
    categories = []
    
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            categories.append("Senior")
        else:
            categories.append("Open")
    return categories