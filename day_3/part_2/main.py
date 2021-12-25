from functools import reduce

def run():
    with open('./day_3/part_2/input.txt','r') as f:
        values = [v.strip() for v in f.readlines()]

    o = oxygen('', values)
    c = co2('', values)
    print(o)
    print(c)
    print(int(o,2) * int(c,2))

def oxygen(reduction, values):
    if len(values[0]) == 0:
        return reduction
    if len(values) == 1:
        reduction += values[0]
        return reduction
    ones = sum(int(v[0]) for v in values)
    zeros = len(values) - ones
    reduction += '0' if zeros > ones else '1'
    values_filtered = filter(lambda x: x[0] == reduction[-1], values)
    values = [v[1:] for v in values_filtered]
    return oxygen(reduction, values)

def co2(reduction, values):
    if len(values[0]) == 0:
        return reduction
    if len(values) == 1:
        reduction += values[0]
        return reduction
    ones = sum(int(v[0]) for v in values)
    zeros = len(values) - ones
    reduction += '1' if ones < zeros else '0'
    values_filtered = filter(lambda x: x[0] == reduction[-1], values)
    values = [v[1:] for v in values_filtered]
    return co2(reduction, values)

    


    


if __name__=='__main__':
    run()