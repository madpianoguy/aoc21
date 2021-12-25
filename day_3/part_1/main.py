from functools import reduce

def run():
    with open('./day_3/part_1/input.txt','r') as f:
        values = [v.strip() for v in f.readlines()]

    g = ''
    e = ''
    b = len(values[0])
    for i in range(0,b):
        zeros = 0
        ones = 1
        for v in values:
            print(v, i)
            if v[i] == '0':
                zeros += 1
            else:
                 ones += 1
        g += '0' if zeros > ones else '1'
        e += '1' if zeros > ones else '0'

    g_val = int(g, 2)
    e_val = int(e, 2)
    print(g,g_val,e, e_val, g_val * e_val)


    


if __name__=='__main__':
    run()