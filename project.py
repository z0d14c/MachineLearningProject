# CS4375 Machine Learning Project
# arg1 trainingfile
# arg2 testfile
# arg3 attributefile (may be hardcoded instead)
import numpy as np
from sklearn.naive_bayes import GaussianNB
import util
import sys
# instantiate args
# arg1 = training data path
# arg2 = test data path
args = sys.argv
# load training/test data
# training/testdata will NOT have class value,  i.e. it will only have the other features
(trainingdata, trainingclasses) = util.readData(args[1])
(testdata, testclasses) = util.readData(args[2])

trainingdata = np.array(trainingdata)
trainingclasses = np.array(trainingclasses)
# load test data (testclasses not used)

classifier = GaussianNB()
classifier.fit(trainingdata, trainingclasses)

predictedVals = classifier.predict(trainingdata)
# what's my accuracy?
util.printAccuracy(predictedVals, trainingclasses)