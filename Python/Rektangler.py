h = 0
b = 0
z = 0
x = 0

while b < 1000:
    h += 1
    if h == 1000:
        b += 1
        h = 0
    a = h * b
    o = 2*h + 2*b

    if a == o:
        print('------------------')
        print('Højde: ' + str(h))
        print('Bredde: ' + str(b))
        print('------------------')
        x = h
        z = b