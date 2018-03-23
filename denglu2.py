#!/bin/bash/env  python


i= 1


while i <= 3:
	user = input("User:")
	pwd  = input("PassWord:")
	i += 1
	if user == "galaxy" and pwd == "password":
		print("Session!")
	else:
		print("Falte!")
		continue