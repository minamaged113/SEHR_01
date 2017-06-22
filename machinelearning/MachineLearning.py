import sys
#sys.path.insert(0, '/home/mina-ubuntu/sehr_project/machinelearning')
import numpy as np
from normalizeData import normalizeData
from getInputFeatures import InputFeatures
from sklearn import svm
from normalizeInputData import normalizeInputData
import scipy.io
def ESP(s):
    #x=normalizeData()
    #np.savetxt('Training Data.txt', x)
    x1=s.get("k1")
    y1=x1.split(",")
    z1 = [float(i) for i in y1]
    z1=np.array(z1)
    x2=s.get("k2")
    y2=x2.split(",")
    z2= [float(i) for i in y2]
    z2=np.array(z2)

    mat1 = scipy.io.loadmat("NO.mat")
    

    No1=mat1["dataM1NO"]
    No2=mat1["dataM2NO"]
    

    feature_no1=InputFeatures(No1[1,:],100)
    feature_no2=InputFeatures(No2[1,:],100)
    feature_no = np.concatenate((feature_no1,feature_no2))
    x=normalizeInputData(feature_no)
    meanNoise1 = np.amax(feature_no1[0:-1])
    meanNoise2 = np.amax(feature_no2[0:-1])
    x=x.reshape(1, -1)

    feature_Like1=InputFeatures(z1,meanNoise1)
    feature_Like2=InputFeatures(z2,meanNoise2)
    feature_Like = np.concatenate((feature_Like1,feature_Like2))
    y=normalizeInputData(feature_Like)
    y=y.reshape(1, -1)

    """
    mat2 = scipy.io.loadmat("Like.mat")
    mat3 = scipy.io.loadmat("Love.mat")

    Like1=mat2["dataM1Like"]
    Like2=mat2["dataM2Like"]
    Love1=mat3["dataM1Love"]
    Love2=mat3["dataM2Love"]

    feature_Like1=InputFeatures(Like1[11,:],meanNoise1)
    feature_Like2=InputFeatures(Like2[11,:],meanNoise2)
    feature_Like = np.concatenate((feature_Like1,feature_Like2))
    y=normalizeInputData(feature_Like)
    y=y.reshape(1, -1)

    feature_Love1=InputFeatures(Love1[13,:],meanNoise1)
    feature_Love2=InputFeatures(Love2[13,:],meanNoise2)
    feature_Love = np.concatenate((feature_Love1,feature_Love2))
    z=normalizeInputData(feature_Love)
    z=z.reshape(1, -1)"""
    return y

def ML(y,path):
    
    trainingData= np.loadtxt(path+'/Training Data.txt')
    predictor = trainingData[:,0:-1]
    response = trainingData[:,-1]

    clf = svm.SVC()
    clf.fit(predictor,response)

    class_no=clf.predict(y)

    """def NO():
        print ("No Gesture.\n")

    def Love():
        print ("Love\n")

    def Like():
        print ("Like\n")


    # map the inputs to the function blocks
    Gesture = {
               1 : NO,
               2 : Like,
               3 : Love,
                
    }
    t=class_no[0]
    Gesture[t]()"""
    t=class_no[0]
    return t
#print(ESP())

