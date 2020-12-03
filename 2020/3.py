#3.py

input_f = '3_input.txt'

def task1():
    with open(input_f, 'r', encoding='UTF8') as in_f:
        fund_map = [i[:-1] for i in in_f.readlines()]
    x, y = 0, 0
    trees = 0
    width = len(fund_map[0])
    for i, map_seg in enumerate(fund_map):
        if map_seg[x] == '#':
            trees += 1
        x = (x + 3) % width
        y += 1        
    print(trees)


def task2():
    with open(input_f, 'r', encoding='UTF8') as in_f:
        fund_map = [i[:-1] for i in in_f.readlines()]
    patterns = [[1, 1], [3, 1], [5, 1], [7, 1], [1,2]]
    trees = [0, 0, 0, 0, 0]
    width = len(fund_map[0])
    for i in range(len(patterns)):
        x, y = 0, 0
        for j in range(0, len(fund_map), patterns[i][1]):
            if fund_map[j][x] == '#':
                trees[i] += 1
            x = (x + patterns[i][0]) % width
            y += 1        
    product = 1
    for i in trees:
        product *= i
    print(product)

def main():
    task1()
    task2()


if __name__ == '__main__':
    main()