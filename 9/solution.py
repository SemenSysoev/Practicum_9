import os

output_filename = os.path.join('simple', 'output.txt')

if not os.path.exists('simple'):
    os.makedirs('simple')

with open('input.txt', 'r', encoding='utf-8') as infile, \
     open(output_filename, 'w', encoding='utf-8') as outfile:
            
    for index, line in enumerate(infile):
        if (index + 1) % 2 == 0:
            outfile.write(line)
