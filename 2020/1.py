#1.py

input_f = '1_input.txt'

def task1():
    with open(input_f, 'r') as inf:
        checked = []
        data = inf.readlines()
        to_check = [int(i[:-1]) for i in data]
        data = [int(i[:-1]) for i in data]
        for i, num1 in enumerate(data):
            for j, num2 in enumerate(to_check):
                if i != j:
                    if num1 + num2 == 2020:
                        print(num1, num2, num1*num2)
            to_check = to_check[1:]

def task2():
    with open(input_f, 'r') as inf:
        data = inf.readlines()
        data = [int(i[:-1]) for i in data]
        to_check = [data[:], data[:], data[:]]
        for i, num1 in enumerate(to_check[0]):
            for j, num2 in enumerate(to_check[1]):
                if i != j:
                    for k, num3 in enumerate(to_check[2]):
                        if num1 + num2 + num3 == 2020:
                            print(num1, num2, num3, num1*num2*num3)
                    to_check[2] = to_check[2][1:]
            to_check[1] = to_check[1][1:]
            to_check[2] = data[:]

def main():
    task1()
    task2()

if __name__ == '__main__':
    main()
