import random
import time

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

def prep(string):
    list_1 = list(string)
    list_1.pop(1)
    for i in range (0, 2):
        x = list_1[i]
        list_1[i] = int(x) - 1
    value = list_1[0] * 8 + list_1[1]
    return(value)

def create_master_list():
    
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

    return(master_list)

def prep_time(int_1):
    rem = int_1 * 3600
    hours = int((int_1 - rem)/3600)
    int_1 = rem
    minutes = int_1 * 60
    hours = int((int_1 - rem)/3600)
    int_1 = rem
    seconds = int_1
    if seconds == 1:
        sec_title = "second"
    else:
        sec_title = "seconds"
        
    if minutes == 1:
        min_title = "minute"
    else:
        min_title = "minutes"

    if hours == 0:
        return("%s %s, and %s %s." % (seconds, sec_title, minutes, min_title))
    elif hours == 1:
        return("1 hour, %s %s, and %s %s." % (seconds, sec_title, minutes, min_title))
    else:
        return("%s hours, %s %s, and %s %s." % (hours, seconds, sec_title, minutes, min_title))
        
    


known_list = []
for i in range (0, 64):
    known_list.append(" ")
count = 0
turn = 0
game = True
print("")
placeholder = format_64(known_list)
start_time = time.strftime("%H:%M:%S")

while game == True:
    
    input_1 = "0-0"
    while validate(input_1) == False:
        print("")
        input_1 = input("Please enter a coordinate. If you would like an example, enter 'example'. ")
        input_1 = input_1.lower()
        if input_1 == "example":
            x = example_cords()
        else:
            toggle = True

    turn = turn + 1
    input_1 = prep(input_1)
    
    if turn == 1:
        master_list = create_master_list()
        while master_list[input_1] != 0:
            master_list = create_master_list()

        tuple_1 = octal_tuple(input_1)
        surround_list = surround(tuple_1)
        surround_list.append(tuple_1)
        length = len(surround_list)
        for i in range (0, length):
            tuple_2 = surround_list[i]
            value = 8 * tuple_2[0] + tuple_2[1]
            x = master_list[value]
            known_list[value] = "%s" % x
            count = count + 1
    else:
        x = master_list[input_1]
        if x == "M":
            known_list[input_1] = x
            game = False
            win = False
        elif known_list[input_1] == str(x):
            toggle = True
        else:
            known_list[input_1] = "%s" % x
            count = count + 1
    
    print("")
    placeholder = format_64(known_list)
    
    if count == 54:
        game = False
        win = True
    else:
        toggle = True

end_time = time.strftime("%H:%M:%S")
start_time = start_time.split(":")
start_value = 3600 * start_time[0] + 60 * start_time[1] + start_time[2]
end_value = 3600 * end_time[0] + 60 * end_time[1] + end_time[2]
delta = end_value - start_value
final_time = prep_time(delta)

if win == True:
    print("")
    print("You won! It took you %s." % final_time)
else:
    print("")
    print("You lost.")

