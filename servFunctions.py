'''
This file holds functions to be
excuted by 'routes.py' which is SEHR's 
back-end file for handling requests
and templates. 
'''
import os,sys,inspect,re
import json
import numpy as np

CWD = os.getcwd()

CWD += "/machinelearning"

# print(CWD)

sys.path.insert(0, CWD)

from MachineLearning import *

global gestures
gestures = list()

def readCounter(filename):
	'''
	readCounter(filename)
		A function to read the counter value
		from the counter text file in the server
		side, in SEHR the counter text file
		is called 'count.txt'.
	USAGE: 
		To use this function in your python code
		write: servFunctions.readCounter('count.txt')
	INPUTS:
		- filename: (string) counter text file name.
	RETURNS:
		- value: (int) which is the integer written
		in the first line of the text file.
	'''
	fhand = open(filename,"r")
	value = fhand.readline()
	fhand.close()
	return int(value)


def writeCounter(filename,countVal):
	'''
	writeCounter(filename,countVal)
		A function to write the counter value
		to the counter text file in the server
		side, in SEHR the counter text file
		is called 'count.txt'.
	USAGE: 
		To use this function in your python code
		write: servFunctions.writeCounter('count.txt',<integer>)
	INPUTS:
		- filename: (string) counter text file name.
		- countVal: (int) new counter value.
	RETURNS:
		void.
	'''
	fhand = open(filename,"w")
	fhand.truncate()
	dummy = str(countVal)
	fhand.write(dummy)
	return


def getGesture(strList):
	'''
	<    Function definition needed   >
	'''
	global gestures
	global CWD
	
	#data  = json.loads(a)[0]
	#result =  data['k1']
	#floatList 	= [float(i) for i in strList]
	y 			= ESP(strList)
	z 			= ML(y,CWD)
	
	# if len(gestures)<10:
	# 	gestures.append(strSum)
	# else:
	# 	del gestures[0]
	# 	gestures.append(strSum)
	print(z)
	return z

