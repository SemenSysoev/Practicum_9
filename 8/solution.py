with open('input.txt', 'r', encoding='utf-8') as f:
    day_steps = []
    for line in f:
        day_steps.append(int(line))

with open('output.txt', 'w', encoding='utf-8') as f:
    if len(day_steps) == 365:
        months = [31, 28, 31, 30, 
                  31, 30, 31, 31,
                  30, 31, 30, 31]
        day_num = 0
        month_num = 0
        steps = 0
        for day in day_steps:
            day_num += 1
            steps += day
            if day_num == months[month_num]:
                f.write(str(steps // day_num) + '\n')
                month_num += 1
                day_num = 0
                steps = 0
    else:
        months = [31, 29, 31, 30, 
                  31, 30, 31, 31,
                  30, 31, 30, 31]
        day_num = 0
        month_num = 0
        steps = 0
        for day in day_steps:
            day_num += 1
            steps += day
            if day_num == months[month_num]:
                f.write(str(steps // day_num) + '\n')
                month_num += 1
                day_num = 0
                steps = 0
