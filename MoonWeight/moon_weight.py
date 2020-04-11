import sys

def calc_weight(weight):
    return weight * 0.165

def cycle_weight():
    print('Enter the start weight')
    weight = float(sys.stdin.readline())

    print('Enter the yearly increase')
    increase = float(sys.stdin.readline())

    print('Enter the amount of years')
    years_amount = int(sys.stdin.readline())

    for x in range(years_amount + 1): 
        print('Weight after ' + str(x) + ' year: ' + str(calc_weight(weight)))
        weight += increase

cycle_weight()