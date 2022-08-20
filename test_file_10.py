import time

x = time.strftime("%M:%S")
print(x)
time.sleep(2)
y = time.strftime("%M:%S")
print(y)
print(y - x)

