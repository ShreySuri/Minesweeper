def octal_list(x):
    x = list(oct(x))
    x.pop(0)
    x.pop(0)
    length = len(x)
    for i in range (0, length):
        x[i] = int(x[i])
    return(x)


