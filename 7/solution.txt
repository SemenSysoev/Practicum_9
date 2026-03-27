numbers = []
with open('input.txt', 'r', encoding='utf-8') as f:
    for num in f:
        if num != '100' and num != '100\n':
            numbers.append(num)
print(numbers)
with open('input.txt', 'w', encoding='utf-8') as f:
    for num in numbers:
        f.write(num)
