#2.py
input_f = '2_input.txt'

def task1():
    correct_pass = 0
    with open(input_f, 'r', encoding='UTF8') as in_f:
        data = [i[:-1] for i in in_f.readlines()]
    for i in data:
        dash_p = i.find('-')
        colon_p = i.find(':')
        am1 = int(i[:dash_p])
        am2 = int(i[dash_p + 1:colon_p - 2])
        letter = i[colon_p - 1]
        password = i[colon_p + 2:]
        occur = password.count(letter)
        #print(i, am1, am2, letter, password, occur)
        if am1 <= occur <= am2:
            correct_pass += 1
    print(correct_pass)

def task2():
    correct_pass = 0
    with open(input_f, 'r', encoding='UTF8') as in_f:
        data = [i[:-1] for i in in_f.readlines()]
    for i in data:
        dash_p = i.find('-')
        colon_p = i.find(':')
        pos1 = int(i[:dash_p])
        pos2 = int(i[dash_p + 1:colon_p - 2])
        letter = i[colon_p - 1]
        password = i[colon_p + 2:]
        #print(i, am1, am2, letter, password, occur)
        matches = int(password[pos1 - 1] == letter) + int(password[pos2 - 1] == letter)
        if matches == 1:
            correct_pass += 1
    print(correct_pass)
    

def main():
    #task1()
    task2()

if __name__ == '__main__':
    main()