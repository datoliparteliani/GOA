list = ["apple", "banana", "cherry", "apple", "mango", "apple"]

element_to_remove = "apple"

item_count = list.count(element_to_remove)

if element_to_remove in list:
    list.remove(element_to_remove)

print(f"element {element_to_remove} appeared {item_count} times.")
print(f"updated list: {list}")