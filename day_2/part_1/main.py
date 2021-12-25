

def run():
    with open('./day_2/part_1/input.txt','r') as f:
        values = [v.split(' ') for v in f.readlines()]
    values = [(v[0], int(v[1])) for v in values]

    x = 0
    y = 0
    
    for dir, mag in values:
        if dir == 'forward':
            x += mag
        elif dir == 'down':
            y += mag
        else:
            y -= mag

    print(x*y)
    return x*y

    


if __name__=='__main__':
    run()