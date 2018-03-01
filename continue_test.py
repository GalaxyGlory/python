#!/root/.pyenv/shims/python

import time

i = 1

while True:
    if i == 7:
        i += 1
        continue

    print(i)
    if i == 10:
        break
    i += 1
