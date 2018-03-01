#!/root/.pyenv/shims/python

import time

i = 1
flag = True

while flag:
    print(i)
    if i == 10:
        flag = False
    i = i+1
    time.sleep(1)
else:
    print("End")
