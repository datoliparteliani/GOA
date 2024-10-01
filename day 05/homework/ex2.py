score = int(input("enter your score: "))

is_A = score>=9
is_B = 8<=score<9
is_C = 7<=score<8
is_D = 6<=score<7
is_F = score<6

print("score:", score)
print("is_A:", is_A)
print("is_B:", is_B)
print("is_C:", is_C)
print("is_D:", is_D)
print("is_F:", is_F)
