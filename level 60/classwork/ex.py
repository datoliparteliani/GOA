def count_arara(n):
    dict = {1: "anane", 2: "adak"}
    adak = n // 2
    anane = n % 2
    total = []
    
    for i in range(adak):
        total.append(dict[2])
    for i in range(anane):
        total.append(dict[1])
    
    return " ".join(total)