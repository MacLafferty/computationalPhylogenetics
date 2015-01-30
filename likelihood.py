#! /usr/bin/env python
from math import factorial as fact
import scipy

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

def genLikelihoods(n,k,pIncrement):
	valueDict={}
	step=0
	while step <= 1:
		value=Bernoulli(n,k,step)
		valueDict[step]=value
		step += pIncrement
	
	return valueDict
	
	
	
N = 5
K = 3
P = 0.05 # Change this and repeat

myDictionary=genLikelihoods(N,K,P)
	

#print myDictionary[.55]
print myDictionary[.6]	
print myDictionary[.65]
	
