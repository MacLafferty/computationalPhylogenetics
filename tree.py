#! /usr/bin/env python
import node

class tree:

	def __init__(self,treeString):
		"""
			initialize tree by adding child nodes to the root according to newick string
		"""
		self.treeString=treeString
		if self.checkString(self.treeString) == True:
			self.root=node.node(None)
			self.currNode=self.root
			self.buildTree(self.treeString)
			"""once information from buildTree is assigned to individual nodes, 
			the nodes then parse that information into names, branch lengths, etc
			recursive function allows the call to be made only to the root"""
			#use this step to do likelihood calculation
			self.root.processInfo()
		else:
			#change to an error in long run
			print "improperly formatted newick string"

	def checkString(self,newick):
		"""
			checks newick string to see if parentheses are balanced and commas are present between groups
		"""
		isBalanced=True
		stack=[]
		foundComma=False
		for char in newick:
			if char == "(":
				stack.append(char)
			elif char == ",":
				foundComma=True
			elif char == ")":
				if foundComma==True:
					stack.pop()
					foundComma=False
				else:
					isBalanced=False
					break
			else:
				pass
		if len(stack) != 0:
			isBalanced=False
		return isBalanced
	
	def buildTree(self,newick):
		"""
			iterates through the newick string given for tree construction, 
		"""
		for i in range(len(newick)):
			if newick[i] == "(":
				self.currNode.children.append(node.node(self.currNode))
				self.currNode=self.currNode.children[0]
			#polytomy support enabled
			elif newick[i] == ",":
				self.currNode=self.currNode.parent
				self.currNode.children.append(node.node(self.currNode))
				self.currNode=self.currNode.children[-1]
			elif newick[i] == ")":
				self.currNode=self.currNode.parent
			else:
				self.currNode.info+=newick[i]
