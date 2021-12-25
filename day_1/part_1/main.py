from functools import reduce


def run():
    with open('./day_1/part_1/input.txt','r') as f:
        values = [int(v) for v in f.readlines()]

    increases = 0
    for index in range(1,len(values)):
        if values[index] > values[index-1]:
            increases += 1
    print(increases)
    return increases


if __name__=='__main__':
    run()