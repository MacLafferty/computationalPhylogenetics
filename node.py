#! /usr/bin/env python
import re
import MC
class node:
	def __init__(self,parent):
		self.parent=parent
		self.children=[]
		self.info=""
		self.name=""
		self.branchLength=0.0
	#allows for presence and absence of branch lengths
	def processInfo(self):
		regex=re.search("(\w+)*(:(0\.\d+)*)",self.info)		
		if self.parent != None and regex.group(1) != None:
				#has a name/is terminal node
				self.name=regex.group(1)
		else:
			self.name+="("
			for child in self.children:
				child.processInfo()
				self.name+=child.name+","
			self.name+=")"
		if self.parent != None:
			self.branchLength=regex.group(3)
			
