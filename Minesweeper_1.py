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
        print("%s,%s" % (x, y))
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
    

row_1 = []
row_2 = []
row_3 = []
row_4 = []
row_5 = []
row_6 = []
row_7 = []
row_8 = []

column_1 = []
column_2 = []
column_3 = []
column_4 = []
column_5 = []
column_6 = []
column_7 = []
column_8 = []


for i in range (0, 8):
    sub_list = []
    for j in range (0, 8):
        index = 8 * i + j
        sub_list.append(master_list[index])
    print(sub_list)

for i in range (0, 64):
    i = octal_tuple(i)
    first = i[0]
    second = i[1]
    if first == 0:
        row_1.append(i)
    elif first == 1:
        row_2.append(i)
    elif first == 2:
        row_3.append(i)
    elif first == 3:
        row_4.append(i)
    elif first == 4:
        row_5.append(i)
    elif first == 5:
        row_6.append(i)
    elif first == 6:
        row_7.append(i)
    elif first == 7:
        row_8.append(i)
    else:
        print("Something went wrong. ")

    if second == 0:
        column_1.append(i)
    

