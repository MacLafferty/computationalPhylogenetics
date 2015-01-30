#! /usr/bin/env python
from math import factorial as fact

def boundedFactorial(min,max):
	"""
		a function which multiplies all numbers between two positive integer values
	"""
	#only executes if input is proper (i.e. min is smaller than max)
	if min < max and min > 0 and max > 0:
		total=max
		print 
		while max > min:
			max -= 1
			total= total * max	
		return total
	else:
		print max
		print min
		return -1
		
		

def easyCoefficient(n,k):
	val = boundedFactorial(n-(k-1),n) / fact(k)
	return val
	
def Bernoulli(n,k,p):
	binom=easyCoefficient(n,k)
	bern=binom * pow(p,k) * pow ((1-p),(n-k))
	return bern

n = 5
p = 0.5 # Change this and repeat

import scipy
valueList=[]
for i in range(0,105,5):
	step=i/float(100)
	print step
	value=Bernoulli(5,5,step)
	print value
	valueList.append((value,step))
	
for item in valueList:
	print item
