# 4.py
import re

f_input = '4_input.txt'

def format_passport_data(input_data):
    sort_data = []
    current = ''
    for i in input_data:
        if i != '':
            current += i + ' '
        else:
            sort_data.append(current[:-1])
            current = ''
    sort_data.append(current[:-1])
    formatted_data = []
    for i in sort_data:
        current = {}
        elements = i.split(' ')
        for j in elements:
            key, val = j.split(':')
            current[key] = val
        formatted_data.append(current)
    return(formatted_data)

def height_check(raw_height):
    height = int(re.sub('[^0-9]','', raw_height))
    inches = True
    passed = False
    if 'cm' in raw_height:
        inches = False
    if inches:
        if 59 <= height <= 76:
            passed = True
    else:
        if 150 <= height <= 193:
            passed = True
    return passed

def hair_color_check(hcl):
    pattern = re.compile('#[a-z0-9]{6}')
    q = pattern.match(hcl)
    if q:
        if q.end() == len(hcl):
            return True
    return False

def eye_color_check(ecl):
    valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if ecl in valid:
        return True
    return False

def passport_id_check(pid):
    pattern = re.compile('[0-9]{9}')
    q = pattern.match(pid)
    if q:
        if q.end() == len(pid):
            return True
    return False

def task1():
    required = ['byr', 'iyr','eyr','hgt','hcl','ecl','pid']
    with open(f_input, 'r', encoding='UTF8') as in_f:
        raw_data = [i[:-1] for i in in_f.readlines()]
    formatted = format_passport_data(raw_data)
    n_valid = 0
    for element in formatted:
        valid = True
        for cur_req in required:
            if cur_req not in element:
                valid = False
        if valid:
            n_valid += 1
    print(n_valid)


def task2():
    rules = {'byr' : lambda x: 1920 <= int(x) <= 2002, 'iyr' : lambda x: 2010 <= int(x) <= 2020, 'eyr' : lambda x: 2020 <= int(x) <= 2030,
             'hgt': lambda x: height_check(x), 'hcl': lambda x: hair_color_check(x), 'ecl' : lambda x: eye_color_check(x),
             'pid' : lambda x: passport_id_check(x)}
    with open(f_input, 'r', encoding='UTF8') as in_f:
        raw_data = [i[:-1] for i in in_f.readlines()]
    formatted = format_passport_data(raw_data)
    n_valid = 0
    for element in formatted:
        #print(element)
        valid = True
        failed = []
        for rule in rules:
            if rule in element:
                if not rules[rule](element[rule]):
                    valid = False
                    failed.append(str(rule + ' ' + element[rule]))
            else:
                valid = False
        if valid:
            n_valid += 1
        print(failed)
    print(n_valid)




def main():
    task1()
    task2()


if __name__ == '__main__':
    main()
