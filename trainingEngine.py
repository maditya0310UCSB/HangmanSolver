from __future__ import division
import time
import itertools
import collections
import re
import string
import math
import sys
import numpy as np


# start = time.time()


#######
#Model Development 
# From now we will call size as length of the word
# Steps - 
# 1) Create the dictionary with keys as length of word and elements as words
# 2) find the word count list i.e. list of all the words
# 3) for each word length, calculate the frequency of the most occuring character

class Node:

	def __init__(self,charac,left=None,right=None): #constructor of class

		self.char =charac
		self.left = None  #left leef
		self.right = None #right leef


def maxFreqCharFn(wordList, dontCareChar):
	#find max word frequency in list of words
	charFreq = (collections.Counter([letter for sublist in map(set,wordList) for letter in sublist]))

	mostFreq = charFreq.most_common(30)

	if dontCareChar == []:
		return mostFreq[0][0][0]
	for i in range(len(mostFreq)):
		if mostFreq[i][0][0] not in dontCareChar:
			return	mostFreq[i][0][0]


def wordsWithoutChar(wordList,charac):
	
	if charac==None:
		return []
	else:
		return [word for word in wordList if charac not in word]


def wordsWithChar(wordList,charac):
	
	if charac==None:
		return []
	else:
		return [word for word in wordList if charac in word]


def createTree(wordList, dontCareChar):

	charac = maxFreqCharFn(wordList, dontCareChar)

	dontCareChar = dontCareChar + [charac]
	root = Node(charac)

	wrdListExcldMaxFreqChar  = wordsWithoutChar(wordList,charac)
	wrdListIncldMaxFreqChar  = wordsWithChar(wordList,charac)

	root = Node(charac)
	if len(wrdListExcldMaxFreqChar) <1:
		# print "len(wrdListExcldMaxFreqChar)",len(wrdListExcldMaxFreqChar)
		root.left = None
		# return root
	else:
		root.left = createTree(wrdListExcldMaxFreqChar, dontCareChar)


	if len(wrdListIncldMaxFreqChar) <1:
		# print "len(wrdListIncldMaxFreqChar)",len(wrdListIncldMaxFreqChar)
		root.right = None
		# return root
	else:
		root.right = createTree(wrdListIncldMaxFreqChar, dontCareChar)

	return root

def createPrimaryNode(wordList):
	dontCareChar =[]
	maxFreqChar = maxFreqCharFn(wordList,[])
	

	dontCareChar = dontCareChar + [maxFreqChar]

	root = Node(maxFreqChar)

	wrdListExcldMaxFreqChar  = wordsWithoutChar(wordList,maxFreqChar)
	wrdListIncldMaxFreqChar  = wordsWithChar(wordList,maxFreqChar)


	if len(wrdListExcldMaxFreqChar) <5:
		root.left = None
	else:
		root.left = createTree(wrdListExcldMaxFreqChar, dontCareChar)


	if len(wrdListIncldMaxFreqChar) <5:
		root.right = None
	else:
		root.right = createTree(wrdListIncldMaxFreqChar, dontCareChar)

	return root



def training(dataset):

	start = time.time()

	#Create dictionary for all the words
	d=collections.defaultdict(list)
	for word in dataset:
		d[len(word)].append(word)


	charCount = d.keys()
	charCount = np.asarray(charCount)
	charCount = charCount[(np.asarray(charCount)<=23) & (np.asarray(charCount)>=2)] 

# 	print d[2]
	listRootNodes =[]

	for i in charCount:
		wordList = d[i]

		listRootNodes.append(createPrimaryNode(wordList))

	defaultTreeNode = createPrimaryNode(dataset)


	print "Training Complete"

	end = time.time()
	trainingTime = end - start

	print "Training Time:", round(trainingTime,3), "seconds"

	return listRootNodes, defaultTreeNode, charCount