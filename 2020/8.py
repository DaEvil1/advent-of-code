#8.py

f_input = '8_input.txt'

class AccumulatorVal:

    def __init__(self, data):
        self.instructions = {'nop': self._nop, 'acc': self._acc, 'jmp' : self._jmp}
        self.data = data
        self.infinite = False
        self.accumulator = 0
        self.positions = []
        self.current = {'operator': None, 'value': None}
    
    def Run(self):
        self.iter = 0
        while True:
            if self.iter in self.positions:
                self.infinite = True
                break
            elif self.iter > len(self.data) - 1:
                break
            self.positions.append(self.iter)
            current = self.data[self.iter]
            self.current['operator'] = current[4]
            self.current['value'] = int(current[5:])
            instr = current[:3]
            self.instructions[instr]()
        
    def Fix(self):
        for i, dat in enumerate(self.data):
            self.positions = []
            self.infinite = False
            self.accumulator = 0
            if dat[:3] == 'nop':
                self.data[i] = 'jmp' + dat[3:]
            elif dat[:3] == 'jmp':
                self.data[i] = 'nop' + dat[3:]
            self.Run()
            if self.infinite == False:
                break
            self.data[i] = dat

    def _nop(self):
        self.iter += 1

    def _acc(self):
        self.iter += 1
        if self.current['operator'] == '+':
            self.accumulator += self.current['value']
        else:
            self.accumulator -= self.current['value']


    def _jmp(self):
        if self.current['operator'] == '+':
            self.iter += self.current['value']
        else:
            self.iter -= self.current['value']

def task1():
    with open(f_input, 'r', encoding='UTF8') as in_f:
        data = [i.rstrip() for i in in_f.readlines()]
    accval = AccumulatorVal(data)
    accval.Run()
    print('task1:', accval.accumulator)

def task2():
    with open(f_input, 'r', encoding='UTF8') as in_f:
        data = [i.rstrip() for i in in_f.readlines()]
    accval = AccumulatorVal(data)
    accval.Fix()
    print('task2:', accval.accumulator)

def main():
    task1()
    task2()

if __name__ == '__main__':
    main()