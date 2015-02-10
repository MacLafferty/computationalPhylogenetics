#! /usr/bin/env python
from math import factorial as fact
from scipy.stats import binom

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
	"""
		calculate the binomial coefficient by canceling out some of the factorial multiplication
	"""
	val = boundedFactorial(n-(k-1),n) / fact(k)
	return val
	
def Bernoulli(n,k,p):
	"""
		return likelihood for bernoulli trial
	"""
	binom=easyCoefficient(n,k)
	bern=binom * pow(p,k) * pow ((1-p),(n-k))
	return bern
	
def genLikelihoods(n,k,pIncrement):
	"""
		creates a dictionary filled with keys = p values sized by arguement pIncrement
		values of dictionary are a tuple with format (ML value, ML ratio)
	"""
	valueDict={}
	step , maxVal = 0 , 0
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
	
def peakFinder(n,k,pStart,diff):
	"""
	given a starting p value and step size, function will find ML for N choose K
	"""
	pCurr=pStart
	while diff > .0001:
		pDown,pUp=pCurr - diff , pCurr + diff
		currML,downML,upML=Bernoulli(n,k,pCurr) , Bernoulli(n,k,pDown) , Bernoulli(n,k,pUp)
		while currML < downML or currML < upML:
			if downML > currML:
				pCurr=pDown
			elif upML > currML:
				pCurr=pUp
			pDown,pUp=pCurr - diff , pCurr + diff
			currML,downML,upML=Bernoulli(n,k,pCurr) , Bernoulli(n,k,pDown) , Bernoulli(n,k,pUp)
		#reduce size of diff by 1/2 to fine-tune
		diff *= .5
	return pCurr, currML

#test peak-find function
P,ML=peakFinder(100,17,.35,.1)

print "P:",str(P)
print "ML:",str(ML)

#pick a p value, assign number of trials and replicates per trial desired
#creates a list of lists containing replicate values for each trial

trueP=.72
numDraws=1000
N=100
draws=[]
for x in range(numDraws):
	draw=binom.rvs(N,trueP)
	draws.append(draw)
	
	
print draws

"""
MLvals = []
likelivals = []
for draw in drawlist:
	likelihood = Bernoulli(N, draw, trueP)
	peakFinder()
	maxlikeli, probability = hillclimb((val, trials), 0.5)
	likelivals.append(likes)
	MLvals.append(maxlikeli)
"""
