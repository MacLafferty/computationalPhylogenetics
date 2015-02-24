#! usr/bin/env python
import numpy as np
import scipy as sp

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

class markovChain:
	#TODO expand to include continuous
	#see notes from Feb 19
	def __init__(self,n,allProbs,st=("a","b")):
		self.chain=[]
		self.states=st
		self.allProbs=allProbs
		
		#after having defined major variables, we want to decide b/w discreet v continuous
		
		#draws starting state
		#TODO: set starting frequencies to something other than equal
		self.currState=discSamp(st,[1.0/len(st) for x in st])
		self.chain.append(self.currState)
		#begin with range 1, as starting state is already given
		for step in range(1,n):
			#TODO: change to np matrix
			probs = self.allProbs[st.index(self.currState)]
			self.currState=discSamp(st,probs)
			self.chain.append(self.currState)
	
	#adds n steps to discreet chain
	def extendChain(self,numSteps):
		self.currState=self.chain[-1]
		for step in range(len(self.chain),len(self.chain)+numSteps):
			#TODO np matrix
			probs = self.allProbs[self.states.index(self.currState)]
			self.currState=discSamp(self.states,probs)
			self.chain.append(self.currState)
	
	def showChain(self):
		print self.chain

#currently developing a separate class of continuous markov chain; eventually merge		
class continuousChain:
	def __init(self,t,allProbs,st=("A","C","G","T")):
		self.chain=[]
		self.states=st
		self.allProbs=allProbs
