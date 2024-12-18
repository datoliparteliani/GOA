def count_positives_sum_negatives(numbers):
    if not numbers:
        return []
    
    positive_count = 0
    negative_sum = 0
    
    for num in numbers:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_sum += num
    
    return [positive_count, negative_sum]