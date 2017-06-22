import sys
sys.path.insert(0, '/home/mina-ubuntu/sehr_project/machinelearning')
import scipy.io
import numpy as np
from scipy import signal
import peakutils
def Features(data,meanNoise):
	A_Reading=data
	A_Reading=A_Reading[:10,2:]
	
	#Mean
	m = (np.mean(A_Reading, axis=1)[np.newaxis]).T


	#Variance								   
	variance = (np.var(A_Reading, axis=1)[np.newaxis]).T


	#Standard Devision						   
	std = (np.std(A_Reading, axis=1)[np.newaxis]).T


	#LogDetector							   
	logDetector = (np.exp(np.mean(np.log10(abs(A_Reading)),axis=1))[np.newaxis]).T


	#PSD 
	psd = (np.sum(np.power(A_Reading,2),axis=1)[np.newaxis]).T


	#Remove the mean of the data to get data normalize
	AreadingNorm = np.subtract(A_Reading,m)

	
	#Peak Value
	PeakValue = (np.amax(abs(AreadingNorm),axis=1)[np.newaxis]).T


	#integral absolute value (area under curve)
	inegralAbsVal = (np.sum(abs(AreadingNorm),axis=1)[np.newaxis]).T


	#max frequency of the signal
	freq = (np.amax (abs(np.fft.fft(AreadingNorm,axis=1)),axis=1)[np.newaxis]).T


	#wave form lenght
	waveformLength =((np.sum(abs(AreadingNorm[:,1::2]-AreadingNorm[:,0::2]),axis=1))+ (np.sum(abs(AreadingNorm[:,2::2]-AreadingNorm[:,1:-1:2]),axis=1))[np.newaxis]).T 
	#no of peaks higher than noise max peak
	drms=meanNoise
	x=AreadingNorm.shape
	AreadingNormFlip = AreadingNorm*-1
	peakNoPos=[]
	peakNoNeg=[]
	for i in range(x[0]):
		peakNoPos = np.append(peakNoPos ,len (peakutils.indexes(AreadingNorm[i,:], thres=0.3, min_dist=drms)))
		peakNoNeg =np.append (peakNoNeg ,len (peakutils.indexes(AreadingNormFlip[i,:], thres=0.3, min_dist=drms)))

	peakNo=(peakNoPos+peakNoNeg[np.newaxis]).T


	 

	#Feature Array
	features = np.concatenate((variance,std,PeakValue,peakNo,inegralAbsVal,freq,waveformLength,logDetector,psd),axis=1)
	Size = features.shape
	#print (Size)
	return features
