import math

while True:
    r = float(input('введите радиус: '))
    area = math.pi * r ** 2
    volume = (3/4) * math.pi * r ** 2
    print('площадь: ', area)
    print('Объём шара: ', volume)