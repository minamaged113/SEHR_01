from getTrainingData import getTrainingData
import numpy as np

trainingData=getTrainingData()
predictor = trainingData[:,0:-1]
response = (trainingData[:,-1][np.newaxis]).T

print(response)
print(predictor.shape)
