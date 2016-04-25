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
(dataDict, classDict) = util.filterByYear(trainingdata, trainingclasses)
classifierDict = {}
for key in dataDict.keys():
    classifierDict[key] = GaussianNB().fit(np.array(dataDict[key]), np.array(classDict[key]))
# trainingdata = np.array(trainingdata)
# trainingclasses = np.array(trainingclasses)
# load test data (testclasses not used)
(testdata, testclasses) = util.readData(args[2])

# classifier = GaussianNB()
# classifier.fit(trainingdata, trainingclasses)
# predictedVals = classifier.predict(trainingdata)

correct = 0
for key in classifierDict.keys():
    x = 0
    predictedVals = classifierDict[key].predict(np.array(dataDict[key]))
    for row in predictedVals:
        if dataDict[key][x][len(trainingdata[0]) - 1] == classDict[key][x]:
            correct += 1
        x += 1
print((correct/len(trainingdata)) * 100)

# attributes = util.readAttributes("data/attr.txt")
