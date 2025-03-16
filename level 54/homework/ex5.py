def two_oldest_ages(ages):
    ages = list(set(ages))
    ages.sort()
    
    return [ages[-2], ages[-1]]