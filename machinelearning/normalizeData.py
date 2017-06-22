import numpy as np
from getTrainingData import getTrainingData

def normalizeData():
	trainingData = getTrainingData()
	size= trainingData.shape
	trainingData[:,8] = trainingData[:,8] / np.linalg.norm(trainingData[:,8])
	trainingData[:,17] = trainingData[:,17] / np.linalg.norm(trainingData[:,17])
	trainingData[:,3] = trainingData[:,3] / np.linalg.norm(trainingData[:,3])
	trainingData[:,10] = trainingData[:,10] / np.linalg.norm(trainingData[:,10])
	return trainingData 



