from functools import reduce


def run():
    with open('./day_1/part_1/input.txt','r') as f:
        values = [int(v) for v in f.readlines()]

    increases = 0
    last = 0
    for index in range(3,len(values)):
        current = sum(values[index-3:index])
        if current > last:
            increases += 1
        last = current
    print(increases)
    return increases


if __name__=='__main__':
    run()