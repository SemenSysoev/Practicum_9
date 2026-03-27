text = []
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        text.append(line.upper())
with open('output.txt', 'w', encoding='utf-8') as f:
    for line in text:
        f.write(line)
