import random

def octal_list(x):
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
    return(x)

def example_cords():
    for i in range (0, 10):
        decimal = random.randint(0, 64)
        octal = octal_list(decimal)
        x = octal[0] + 1
        y = octal[1] + 1
        print("%s,%s" % (x, y))
    return(None)

master_list = []
for i in range (0, 64):
    list_i = octal_list(i)
    tuple_i = tuple(list_i)
    master_list.append(tuple_i)




        
