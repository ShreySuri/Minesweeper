def validate(string):
    check = False
    for i in range (1, 9):
        for j in range (1, 9):
            value = "%s-%s" % (i, j)
            if value == string:
                check = True
            else:
                toggle = True
            
    return(check)

x = validate("8-8")
print(x)
