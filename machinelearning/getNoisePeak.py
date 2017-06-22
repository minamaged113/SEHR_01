import numpy as np

def getNoise(Noise):
	noisePeaks=(np.amax(abs(Noise),axis=1)[np.newaxis]).T
	return noisePeaks
