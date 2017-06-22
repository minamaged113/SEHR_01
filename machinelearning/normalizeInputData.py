import sys
sys.path.insert(0, '/home/mina-ubuntu/sehr_project/machinelearning')
import numpy as np

def normalizeInputData(trainingData): 
	size= trainingData.shape
	trainingData[8] = trainingData[8] / np.linalg.norm(trainingData[8])
	trainingData[17] = trainingData[17] / np.linalg.norm(trainingData[17])
	trainingData[3] = trainingData[3] / np.linalg.norm(trainingData[3])
	trainingData[10] = trainingData[10] / np.linalg.norm(trainingData[10])
	return trainingData 
