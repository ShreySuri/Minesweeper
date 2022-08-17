import random

def octal_tuple(x):
    x = list(oct(x))
    x.pop(0)
    x.pop(0)
    length = len(x)
    if length < 2:
        value = int(x[0])
        x.pop(0)
        x.append(0)
        x.append(value)
    else:
        for i in range (0, length):
            x[i] = int(x[i])
    return(tuple(x))

def octal_list(x):
    x = list(oct(x))
    for i in range (0, 2):
        x.pop(0)
    if len(x) < 2:
        x.append(0)
        x = x.reverse()
    else:
        toggle = True

    return(x)

def octal_to_decimal(tuple_1):
    first = tuple_1[0]
    second = tuple_1[1]
    return(int(first * 8 + second))

    
def example_cords():
    for i in range (0, 10):
        decimal = random.randint(0, 64)
        octal = octal_tuple(decimal)
        x = octal[0] + 1
        y = octal[1] + 1
        print("(%s, %s) --> %s-%s" % (x, y, x, y))
    return(None)

def surround(tuple_1):
    first = tuple_1[0]
    second = tuple_1[1]
    surround_list_1 = []
    surround_list_2 = []
    for i in range (first - 1, first + 2):
        for j in range (second - 1, second + 2):
            surround_list_1.append((i, j))

    for k in range (0, 9):
        x = surround_list_1[k]
        first = x[0]
        second = x[1]
        if first >= 0 and first < 8 and second >= 0 and second < 8:
            surround_list_2.append(x)

    surround_list_2.remove(tuple_1)
    return(surround_list_2)

def format_64(list_64):
    for i in range (0, 8):
        string = "|"
        for j in range (0, 8):
            index = 8 * i + j
            value = list_64[index]
            string = "%s%s   " % (string, value)
        string = "%s|" % string
        print(string)
    return(None)

master_list = []
for i in range (0, 64):
    i = octal_tuple(i)
    master_list.append(i)

mines = 0
while mines < 10:
    x = random.randint(0, 63)
    if master_list[x] != "M":
        master_list[x] = "M"
        mines = mines + 1
    else:
        toggle = True

for i in range (0, 64):
    if master_list[i] != "M":
        surround_list = surround(octal_tuple(i))
        length = len(surround_list)
        mine_count = 0
        for j in range (0, length):
            surround_tuple = surround_list[j]
            num = octal_to_decimal(surround_tuple)
            if master_list[num] == "M":
                mine_count = mine_count + 1
            else:
                toggle = False
        master_list[i] = mine_count
    else:
        toggle = True

known_list = []
for i in range (0, 64):
    known_list.append(" ")

format_1 = format_64(master_list)
game = True
while game == True:
   
                    
    
