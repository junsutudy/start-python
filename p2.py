print('get area of shape.')
print('choose number: 1 for rectangle, 2 for circle.')
n = int(input())
if n == 1:
    w = float(input('w: '))
    h = float(input('h: '))
    area = w * h
    print('w: ', w, 'h: ', h, 'area: ',area)

elif n == 2:
    radius = float(input('radius: '))
    area = radius * radius * 3.14
    print('radius: ', radius, 'area: ', area)

else:
    print('wtf happend to the number? ', n)