#6.py

f_input = '6_input.txt'

def seperate_groups(data):
    groups = []
    current = []
    for i in data:
        if i != '':
            current.append(i)
        else:
            groups.append(current)
            current = []
    if current != []:
        groups.append(current)
    return groups

def count_group_yes(group):
    yeses = ''
    for i in group:
        for j in i:
            if j not in yeses:
                yeses += j
    return len(yeses)

def count_all_group_yes(group):
    yeses = group[0][:]
    for i in group:
        for j in yeses:
            if j not in i:
                yeses = yeses.replace(j, '')
    return len(yeses)

def task1():
    with open(f_input, 'r', encoding='UTF8') as in_f:
        data = [i.rstrip() for i in in_f.readlines()]
    groups = seperate_groups(data)
    total = 0
    for group in groups:
        total += count_group_yes(group)
    print(total)

def task2():
    with open(f_input, 'r', encoding='UTF8') as in_f:
        data = [i.rstrip() for i in in_f.readlines()]
    groups = seperate_groups(data)
    total = 0
    for group in groups:
        total += count_all_group_yes(group)
    print(total)

def main():
    task1()
    task2()

if __name__ == '__main__':
    main()