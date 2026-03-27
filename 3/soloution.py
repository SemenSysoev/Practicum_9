word = ''
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        word += line[0]
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(word)
