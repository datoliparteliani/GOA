database = {}

def AddToDatabase(first_name, last_name, age):
    database["name"] = first_name
    database["surname"] = last_name
    database["age"] = age
    
    return f"updated database: {database}"

print(AddToDatabase("Dato", "Liparteliani", 15))