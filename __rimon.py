import re
import os
import sys
sys.path.insert(0, '/home/mina-ubuntu/sehr_project/machinelearning')
from MachineLearning import *
global gestures
gestures = list()

def getArrSum(strList):
	global gestures
	floatList 	= [float(i) for i in strList]
	y=ESP(floatList)
	z=ML(y)
	strSum		= str(sum(floatList))
	if len(gestures)<10:
		gestures.append(strSum)
	else:
		del gestures[0]
		gestures.append(strSum)

	#return strSum
	return z

