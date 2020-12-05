#5.py

f_input = '5_input.txt'

def calc_binary(input):
    val = 2**len(input) - 1
    for i in range(len(input)):
        switch = 1 - int(input[i])
        val -= switch*(2**(len(input) - i - 1))
    return val

def binaryToSeat(bin_str, format):
    bin_str = bin_str.replace('B', '1').replace('F', '0').replace('L', '0').replace('R', '1')
    row = calc_binary(bin_str[:format[0]])
    seat = calc_binary(bin_str[format[0]:])
    seatid = row*8 + seat
    return row, seat, seatid

def task1():
    with open(f_input, 'r', encoding='UTF8') as in_f:
        data = [i[:-1] for i in in_f.readlines()]
    highest = 0, 0, 0, ''
    for i in data:
        row, seat, number = binaryToSeat(i, [7, 3])
        if number > highest[0]:
            highest = number, row, seat, i
    print(highest)

def task2():
    with open(f_input, 'r', encoding='UTF8') as in_f:
        data = [i[:-1] for i in in_f.readlines()]
    seats = []
    for i in data:
        row, seat, number = binaryToSeat(i, [7, 3])
        seats.append(number)
        seats.sort()
    current = seats[0] - 1
    for i in seats:
        if i - current != 1:
            print(i - 1)
        current = i


def main():
    task1()
    task2()

if __name__ == '__main__':
    main()