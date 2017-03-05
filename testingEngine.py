from __future__ import division
import time
import itertools
import collections
import re
import string
import math
import sys
import numpy as np
import time

def printFn(word,charGuessed):

	word = word
	ln = len(word)

	incompleteStr = "_"*ln
	incompleteStr = list(incompleteStr)

	missedChar =[]

	print ''.join(incompleteStr), " missed:"
	print '\n'	

	for i in range(len(charGuessed)):
	    print "guess: ", charGuessed[i]
	    
	    if charGuessed[i] not in word:        
	        missedChar.append(charGuessed[i])
	        print ''.join(incompleteStr), " missed: ",', '.join(missedChar)
	            
	    if charGuessed[i] in word:
	        for j in range(ln):
	            if word[j] ==charGuessed[i]:
	                incompleteStr[j] = word[j]                    
	        
	        print ''.join(incompleteStr), " missed: ",', '.join(missedChar)
	    print '\n'

def testing(testDataFile,listRootNodes,defaultTreeNode, charCount, inputType):

	start = time.time()


	testDict=collections.defaultdict(list)
	for word in testDataFile:
	    testDict[len(word)].append(word)


	testDictKeys = testDict.keys()

	maxWrongGuess = 6
	correctWordGuess = 0
	wrongWordGuess = 0
	wrongWordGuessStupid = 0
	wrongPrediction = []
	correctPrediction =[]


	for wordSize in testDictKeys:
	    wordList = testDict[wordSize]
	    
	    if wordSize in charCount:
		    modelNeeded =listRootNodes[wordSize-2] # defaultTreeNode    #
	    else:
	    	modelNeeded = defaultTreeNode


	    for word in wordList:
	        distCharInWord = set(word)
	        distCharSize = len(distCharInWord)
	        
	        currentNode = modelNeeded
	        
	        cntWrongCharGuess = 0	        
	        cntCorrectCharGuess = 0

	        charGuessed =[]
	        
	        while cntWrongCharGuess < maxWrongGuess:
	            if currentNode != None:
	                guess = currentNode.char
	                charGuessed.append(guess)

	            elif (currentNode == None) & (cntCorrectCharGuess < distCharSize):
	                wrongWordGuess = wrongWordGuess+1
	                wrongWordGuessStupid = wrongWordGuessStupid+1                
	                break
	            
	            if guess in distCharInWord:
	                cntCorrectCharGuess =cntCorrectCharGuess +1
	                currentNode = currentNode.right
	            if guess not in distCharInWord:
	                cntWrongCharGuess = cntWrongCharGuess +1
	                currentNode = currentNode.left
	                
	            if cntCorrectCharGuess == distCharSize:
	                correctWordGuess = correctWordGuess + 1
	                correctPrediction.append(word)
	                break
	            elif cntWrongCharGuess >= maxWrongGuess:
	                wrongWordGuess = wrongWordGuess+1
	                wrongPrediction.append(word)
	                break

	end = time.time()
	testingTime = (end - start)

	if inputType == '-w':
		printFn(word,charGuessed)

	elif inputType == '-f':
		# print correctPrediction
		print "Number of words tested:", len(testDataFile)
		print "Number of words guessed correctly:", correctWordGuess
		print "Correct Guesses (%):", round(correctWordGuess/len(testDataFile),3)
		print "TestingTime:", round(testingTime,3), "seconds"


if __name__ == '__main__':
	print "testingEngine File"