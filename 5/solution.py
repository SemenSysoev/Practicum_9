nums = []
with open('input.txt', 'r', encoding='utf-8') as f:
    for num in f:
        nums.append(num)
with open('output.txt', 'w', encoding='utf-8') as f:
    try:
        f.write(str((int(nums[0]) / int(nums[1])) + int(nums[2])))
    except ValueError:
        f.write('data error')
    except ZeroDivisionError:
        f.write('division by 0')
