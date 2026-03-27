with open('input.txt', 'r', encoding='utf-8') as f:
    f_condition = f.readline()
    s_condition = 0
    for line in f:
        s_condition += 1
with open('output.txt', 'w', encoding='utf-8') as f:
    try:
        if int(f_condition) == s_condition:
            f.write('Yes')
        else:
            f.write('No')
    except:
        f.write('ERROR')
