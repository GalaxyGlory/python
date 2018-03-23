import time
i = 0

while True:
    i=i+1
    if i == 7:
        continue
    if i == 10:
        break
    time.sleep(1)
    print(i)

