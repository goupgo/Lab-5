def q1():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    squares = [x**2 for x in numbers]
    print(squares)

def q2():
    list1 = ["Hello", "take"]
    list2 = [" Dear", " Sir"]
    list3 = []
    for i in list1:
        for j in list2:
            res = i + j
            list3.append(res)
            print(list3)