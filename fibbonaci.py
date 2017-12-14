#!/usr/bin/python

def fib(n):
	if(n>1):
		return n * fibb(n-1)
	else:
		return 1
		
num = input("Enter a number")
num = int(num)
fibbo = fib(num)	
print(fibbo)	