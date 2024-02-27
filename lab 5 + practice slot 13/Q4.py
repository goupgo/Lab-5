def q1():
    tuple1 = ('Orange', [10, 20, 30], [5, 15, 25])
    print(tuple1[1][1])

def q2():
    tuple1 = (10, 20, 30, 40)
    a, b, c, d = tuple1
    print(a)
    print(b)
    print(c)
    print(d)

def q3():
    tuple1 = (11, 22)
    tuple2 = (99, 98)
    tuple1, tuple2 = tuple2, tuple1
    print('tuple1', tuple1)
    print('tuple2', tuple2)
