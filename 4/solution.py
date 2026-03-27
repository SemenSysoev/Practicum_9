text = []
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if len(line) >= 20:
            text.append(line)
with open('output.txt', 'w', encoding='utf-8') as f:
    for line in text:
        f.write(line)
