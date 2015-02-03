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

#returns dictionary, where keys are various p values and values are a list containing:
#a value representing likelihood
#another value representing likelihood ratio
def genLikelihoods(n,k,pIncrement):
	valueDict={}
	step=0
	maxVal=0
	while step <= 1:
		value=Bernoulli(n,k,step)
		if value > maxVal:
			maxVal=value
		step=round(step,2)
		valueDict[step]=[value]
		step += pIncrement
	step=0
	#calculate ratios, add to list
	while step <= 1:
		step=round(step,2)
		valueDict[step].append(valueDict[step][0]/maxVal)
		step += pIncrement
	return valueDict

myDictionary=genLikelihoods(5,4,.05)

#print values around peak
print myDictionary[.7]
print myDictionary[.75]
print myDictionary[.8]
print myDictionary[.85]
print myDictionary[.9]

myDictionary2=genLikelihoods(20,12,.05)

#print values around peak
print myDictionary[.5]
print myDictionary[.55]
print myDictionary[.6]
print myDictionary[.65]
print myDictionary[.7]
