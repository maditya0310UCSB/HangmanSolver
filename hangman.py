from __future__ import division
import time
import itertools
import collections
import re
import string
import math
import sys
import numpy as np
import trainingEngine
import testingEngine




if __name__ == '__main__':

	if len(sys.argv) < 3:
		print "Usage: %s [-f|-w] [filename|word]" % sys.argv[0]
		exit(0)


	inputType = sys.argv[1]
	testingFile = sys.argv[2]

	trainingFile = 'words_50000.txt'
	dataset = open(trainingFile,'r').read().split('\n')[:-1]

	if inputType == '-f':
		# testingFile = 'wordsOutSampleCheck2.txt'
		testDataFile = open(testingFile,'r').read().split('\n')[:-1]

	elif inputType == '-w':
		testDataFile = [testingFile]		

	modelTree, defaultTreeNode, charCount = trainingEngine.training(dataset)


	testingEngine.testing(testDataFile, modelTree, defaultTreeNode, charCount, inputType)
