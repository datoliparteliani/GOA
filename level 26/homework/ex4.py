def figures():
    for i in range(120):
        for i in range(3):
            print("******")
        
        print()

        for i in range(1, 9, 2):
            print(" " * ((7 - i) // 2) + "*" * i)

        for i in range(2):
            print(" " * ((7 - i) // 2) + "*")

        print()
        
        for i in range(4, 11, 2):
            print(" " * (i) + "*" * i)
        
        print()

figures()