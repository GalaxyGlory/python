import time
i = 1
flag = True

while flag:
    print(i)
    i = i + 1
    if i == 10:
        flag = False
    time.sleep(1)