import random

wordlist = []
special_char = ['@','&','!','*','$']

with open("wikepedia-test.txt",'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()

        for item in word:
            if len(item)==5:
                wordlist.append(item.capitalize())

word = random.choice(wordlist)
schar = random.choice(special_char)
num = random.randint(10,99)

print(word + schar + str(num))
