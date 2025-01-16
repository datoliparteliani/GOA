my_set = {1, 2, 3, 4, 5}

my_set.add(6)
print("add(6):", my_set)

my_set.clear()
print("clear():", my_set)

my_set = set([1, 2, 3, 4, 5])
print("set:", my_set)

another_set = {4, 5, 6, 7}
difference_set = my_set.difference(another_set)
print("difference:", difference_set)

popped_element = my_set.pop()
print("popped element:", popped_element)
print("pop():", my_set)

my_set.remove(2)
print("remove(2):", my_set)

union_set = my_set.union(another_set)
print("union of my_set and another_set:", union_set)