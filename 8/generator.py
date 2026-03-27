import random as r

with open('input.txt', 'w', encoding='utf-8') as f:
    for _ in range(366):
        f.write(str(r.randint(300, 10000)) + '\n')
