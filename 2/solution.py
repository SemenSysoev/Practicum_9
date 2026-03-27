text = []
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line[0] == 'a' or line[0] == 'A':
            text.append(line)
with open('output.txt', 'w', encoding='utf-8') as f:
    for line in text:
        f.write(line)
