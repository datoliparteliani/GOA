numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",]

vowels = "aeiou"

for number in numbers:
    count = 0
    for i in number:
        if i in vowels:
            count += 1
    print(number + ": " + str(count) + " vowels")