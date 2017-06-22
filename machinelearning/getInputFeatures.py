import scipy.io
import numpy as np
from scipy import signal
import peakutils
def InputFeatures(data,meanNoise):
	A_Reading=data
	#A_Reading=A_Reading[:,2:]
	
	#Mean
	m = (np.mean(A_Reading)[np.newaxis]).T


	#Variance								   
	variance = (np.var(A_Reading)[np.newaxis]).T


	#Standard Devision						   
	std = (np.std(A_Reading)[np.newaxis]).T


	#LogDetector							   
	logDetector = (np.exp(np.mean(np.log10(abs(A_Reading))))[np.newaxis]).T


	#PSD 
	psd = (np.sum(np.power(A_Reading,2))[np.newaxis]).T


	#Remove the mean of the data to get data normalize
	AreadingNorm = np.subtract(A_Reading,m)

	
	#Peak Value
	PeakValue = (np.amax(abs(AreadingNorm))[np.newaxis]).T


	#integral absolute value (area under curve)
	inegralAbsVal = (np.sum(abs(AreadingNorm))[np.newaxis]).T


	#max frequency of the signal
	freq = (np.amax (abs(np.fft.fft(AreadingNorm)))[np.newaxis]).T


	#wave form lenght
	waveformLength =((np.sum(abs(AreadingNorm[1::2]-AreadingNorm[0::2])))+ (np.sum(abs(AreadingNorm[2::2]-AreadingNorm[1:-1:2])))[np.newaxis]).T 
	#no of peaks higher than noise max peak
	drms=meanNoise
	x=AreadingNorm.shape
	AreadingNormFlip = AreadingNorm*-1
	peakNoPos = len (peakutils.indexes(AreadingNorm, thres=0.3, min_dist=drms))
	peakNoNeg =len (peakutils.indexes(AreadingNormFlip, thres=0.3, min_dist=drms))
	peakNo=np.array([peakNoPos+peakNoNeg])


	 

	#Feature Array
	features = np.concatenate((variance,std,PeakValue,peakNo,inegralAbsVal,freq,waveformLength,logDetector,psd))
	#Size = features.shape
	#print (Size)
	return features
