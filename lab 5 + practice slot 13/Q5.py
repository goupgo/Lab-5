inp = input('Enter the string: ')
fhandle = open("Count letters.txt", 'w')
lst = []
count_lst = []
sep_chars = []
dict1 = {}
lst.append(inp)
for line in lst:
    split1 = line.split()
    for i in split1:
        count_lst.append(i)

for x in count_lst:
    for c in x:
        sep_chars.append(c)

for char in sep_chars:
    if char not in dict1:
        dict1.setdefault(char, 1)
    else:
        dict1[char] += 1

time = dict1.values()
for q in dict1:
    res = "The letter " + q + " appears " + str(dict1[q]) + " times \n"
    print(res)
    fhandle.write(res)

fhandle.close()

