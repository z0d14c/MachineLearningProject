# CS4375 Machine Learning Project
# arg1 trainingfile
# arg2 testfile
# arg3 attributefile (may be hardcoded instead)
import numpy as np
from sklearn.naive_bayes import GaussianNB
import util
import sys
# instantiate args
args = sys.argv
# load training data
(trainingdata, trainingclasses) = util.readData(args[1])
trainingdata = np.array(trainingdata)
trainingclasses = np.array(trainingclasses)
# load test data (testclasses not used)
(testdata, testclasses) = util.readData(args[2])

classifier = GaussianNB()
classifier.fit(trainingdata, trainingclasses)
predictedVals = classifier.predict(trainingdata)
correct = 0
x = 0
for val in predictedVals:
    if val == trainingclasses[x]:
        correct += 1
    x += 1
print((correct/len(trainingdata)) * 100)
# attributes = util.readAttributes("data/attr.txt")
