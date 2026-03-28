with open('input.txt', 'r', encoding='utf-8') as f:
    date = f.readline()
    num_cells = f.readline()
    cells = []
    for line in f:
        cells.append(line)
with open('output.txt', 'w', encoding='utf-8') as f:
    months = [0, 31, 59, 90, 
              120, 151, 181, 212, 
              243, 273, 304, 334]
    today_date = int(date.split('.')[0]) + months[int(date.split('.')[1]) - 1]
    for cell in cells:
        cell_date = cell.split(' ')[1]
        num_cell_date = int(cell_date.split('.')[0]) + months[int(cell_date.split('.')[1]) - 1]
        if today_date - num_cell_date > 3:
            f.write(cell.split(' ')[0] + '\n')
