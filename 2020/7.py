#7.py

f_input = '7_input.txt'

def fetch_starting_numeric(in_str):
    pos = 0
    result = 0
    for i in range(len(in_str)):
        if not in_str[:i + 1].isnumeric():
            break
        result = int(in_str[:i + 1])
        pos = i + 1
    return result, pos

def decode_sub(sub):
    sub = sub.replace('.', '')
    sub = sub.split(', ')
    sub = [i.replace('bags', '').replace('bag', '') for i in sub]
    sub = [i.strip() for i in sub]
    rules = {}
    if sub != ['no other']:
        for j in sub:
            num, pos = fetch_starting_numeric(j)
            rules[j[pos + 1:]] = num
    return rules

def decode_rules(data):
    bag_rules = {}
    for i in data:
        i = i.split(' contain ')
        root = i[0].replace('bags', '').replace('bag', '')
        root = root.strip()
        rules = decode_sub(i[1])
        bag_rules[root] = rules
    return bag_rules

def check_bags(rules, bags, goal_bag):
    for bag in bags:
        if goal_bag in rules[bag]:
            return True
        else:
            if rules[bag] != {}:
                new_bags = [j for j in rules[bag]]
                result = check_bags(rules, new_bags, goal_bag)
                if result is not None:
                    return result

class CountBags:

    def __init__(self, rules):
        self.rules = rules
        self.data = {'values' : []}
        self.current = None
        self.tree = []
        self.level = 0
    
    def _count(self):
        for i in self.current:
            cur_val = self.current[i]
            if self.level > 0:
                li = self.data['values'][-1][0:self.level]
                li.append(cur_val)
                cur = li
            else:
                cur = [cur_val]
            self.data['values'].append(cur)
            if self.rules[i] != {}:
                self.level += 1
                self.tree.append(self.current)
                self.current = self.rules[i]
                self._count()
        if self.level > 0:
            self.level -= 1
            self.current = self.tree[-1]
            self.tree.pop()

    def sum(self):
        self.bag_sum = 0
        for i in self.data['values']:
            val = 1
            for j in i:
                val = val*j
            self.bag_sum += val

    def count(self, rootbag):
        self.current = self.rules[rootbag]
        self._count()
        self.sum()
        return self.bag_sum


def task1():
    with open(f_input, 'r', encoding='UTF8') as in_f:
        data = [i.rstrip() for i in in_f.readlines()]
    goal_bag = 'shiny gold'
    rules = decode_rules(data)
    gold_bags = 0
    for i in rules:
        if goal_bag in rules[i]:
            gold_bags += 1
    for i in rules:
        bags = [j for j in rules[i]]
        if check_bags(rules, bags, goal_bag):
            gold_bags += 1
    print('task1: ', gold_bags)

def task2():
    with open(f_input, 'r', encoding='UTF8') as in_f:
        data = [i.rstrip() for i in in_f.readlines()]
    root_bag = 'shiny gold'
    rules = decode_rules(data)
    counter = CountBags(rules)
    total_bags = counter.count(root_bag)
    print('task2 :', total_bags)
    

def main():
    task1()
    task2()

if __name__ == '__main__':
    main()