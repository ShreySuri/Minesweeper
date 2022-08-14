import random

def octal_list(x):
    x = list(oct(x))
    x.pop(0)
    x.pop(0)
    length = len(x)
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

        
