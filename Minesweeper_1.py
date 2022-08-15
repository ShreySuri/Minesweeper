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

def example_cords():
    for i in range (0, 10):
        decimal = random.randint(0, 64)
        octal = octal_tuple(decimal)
        x = octal[0] + 1
        y = octal[1] + 1
        print("%s,%s" % (x, y))
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
    

while game == True:
    
