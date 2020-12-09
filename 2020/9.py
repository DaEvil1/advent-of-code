#9.py

f_input = '9_input.txt'
n_sum = 25

def check_sum(check, content):
    for i, num in enumerate(content):
        for j, num2 in enumerate(content):
            if i != j:
                if num + num2 == check:
                    return True
    return False

def task1():
    with open(f_input, 'r', encoding='UTF8') as in_f:
        data = [int(i.rstrip()) for i in in_f.readlines()]
    for i in range(n_sum, len(data)):
        content = [data[j] for j in range(i - n_sum, i)]
        check = check_sum(data[i], content)
        if not check:
            return data[i]

def task2(faulty_num):
    with open(f_input, 'r', encoding='UTF8') as in_f:
        data = [int(i.rstrip()) for i in in_f.readlines()]
    for i in range(2, len(data)):
        for j in range(len(data)):
            if j + i < len(data):
                cur = [data[k] for k in range(j, j+i)]
                if sum(cur) == faulty_num:
                    return min(cur) + max(cur)

def main():
    faulty_num = task1()
    print('Task 1:', faulty_num)
    weakness = task2(faulty_num)
    print('Task 2:', weakness)

if __name__ == '__main__':
    main()