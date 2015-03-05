#! usr/bin/env python
import copy
import numpy as np
import scipy as sp
from scipy.stats import expon

def discSamp(events,probs):
    """
    This function samples from a list of discrete events provided in the events
    argument, using the event probabilities provided in the probs argument. 
    These lists must:
        - Be the same length
        - Be in corresponding orders
    Also, the probabilities in probs must sum to 1.
    """
    ranNum = sp.random.random()
    cumulProbs = []
    cumulProbs.extend([probs[0]])
    for i in range(1,len(probs)):
        cumulProbs.extend([probs[i]+cumulProbs[-1]])
    for i in range(0,len(probs)):
        if ranNum < cumulProbs[i]:
           return events[i]
    return None


#currently developing a separate class of continuous markov chain; eventually merge		
class continuousChain:
	def __init__(self,Q,V=1.0,states=("A","C","G","T")):
		#assign arguments
		self.Q , self.V , self.states = Q , V , states
		
		#Q matrix used to create a matrix of normalized transition probabilities between states
		self.transProbs=[]
		i=0
		for row in self.Q:
			self.transProbs.append(copy.deepcopy(row))
			denom=abs(self.transProbs[i].pop(i))
			j=0
			for num in self.transProbs[i]:
				num=num/denom
				self.transProbs[i][j]=num
				j+=1
			i+=1
			
		self.chain=[]
		self.waitTimes=[]
		self.totalTime=0
		
		#set initial state
		self.chain.append(discSamp(self.states,[1.0/len(self.states) for x in self.states]))
		
		print "self:",self.Q
		while self.totalTime < self.V:
			#draw wait time
			print "chain",self.chain
			index=self.states.index(self.chain[-1])
			print "index:",index
			wait=expon.pdf(abs(self.Q[index][index]))
			#append wait time to list
			self.waitTimes.append(wait)
			#add wait time to total Time
			self.totalTime += wait
			
			
			if self.totalTime < self.V:
				index=self.states.index(self.chain[-1])
				probs=self.transProbs[index]
				#remove current state from list of possible outcomes
				newStates=[]
				newStates.extend(self.states)
				newStates.pop(index)
				substitution=discSamp(newStates,probs)
				print "sub:",substitution
				self.chain.append(substitution)
			#draw new state based on previous state (pretty much identical to discreet chain
	
Qmatrix=[[-1.2,.4,.4,.4],[.2,-1,.5,.3],[.25,.38,-.8,.17],[.47,.57,.36,-1.4]]			
testChain=continuousChain(Qmatrix)
print testChain.chain
print testChain.waitTimes
