import random

upper_case = ["A","B","C","D","E"]
lower_case = ["a","b","c","d","e"]
num = ['1','2','3','4','5']
special_char = ['@','&','!','*','$']

passw = random.choice(upper_case)+random.choice(lower_case)+random.choice(num)+random.choice(special_char)+random.choice(upper_case)+random.choice(lower_case)+random.choice(num)+random.choice(special_char)

print(passw)
