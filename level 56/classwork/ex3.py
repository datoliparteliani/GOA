def captianjack(gold_coin):
    if gold_coin == 0:
        return "ekipaji ajanyda"
    ships = {
        "1": 150,
        "2": 200,
        "3": 250,
        "4": 300,
        "5": 350,
    }
    chosen = input("airchie gemi: ")
     
    if chosen in ships:
        if gold_coin < ships[chosen]:
            return "ekipaji ajanyda"
        return f"shen warmatebit iyide {chosen} gemi"