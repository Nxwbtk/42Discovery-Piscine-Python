#! /usr/bin/python3
try:
	num = int(input("Enter a number\n"))
	for i in range(0, 10):
		print(f'{i} x {num} = {num * i}')
except:
	print("Error")
	exit()