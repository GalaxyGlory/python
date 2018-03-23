#!/bin/bash/env  python

i = 1
sum = 0



while True:

	if i % 2 == 0 and i <= 100:
		sum = sum	
	elif i %2 == 1 and i <= 100:
		sum = sum + i
	else:
		break
	i =i + 1
print(sum)