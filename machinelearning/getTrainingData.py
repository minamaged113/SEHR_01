from getFeatures import Features
from getNoisePeak import getNoise
import numpy as np
import scipy.io

def getTrainingData():
	mat1 = scipy.io.loadmat("NO.mat")
	mat2 = scipy.io.loadmat("Like.mat")
	mat3 = scipy.io.loadmat("Love.mat")


	feature_no1=Features(mat1["dataM1NO"],100)
	feature_no2=Features(mat1["dataM2NO"],100)
	feature_no = np.concatenate((feature_no1,feature_no2),axis=1)
	meanNoise1 = np.amax(feature_no1[0:-1,3])
	meanNoise2 = np.amax(feature_no2[0:-1,3])


	feature_Like1=Features(mat2["dataM1Like"],meanNoise1)
	feature_Like2=Features(mat2["dataM2Like"],meanNoise2)
	feature_Like = np.concatenate((feature_Like1,feature_Like2),axis=1)


	feature_Love1=Features(mat3["dataM1Love"],meanNoise1)
	feature_Love2=Features(mat3["dataM2Love"],meanNoise2)
	feature_Love = np.concatenate((feature_Love1,feature_Love2),axis=1)


	trainingSet= np.concatenate((feature_no,feature_Like,feature_Love),axis=0)
	Y=np.concatenate((np.ones((10,1)),(2*np.ones((10,1))),(3*np.ones((10,1)))),axis=0)

	allData = np.concatenate((trainingSet,Y),axis=1)
	return allData


