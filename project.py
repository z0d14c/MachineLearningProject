# CS4375 Machine Learning Project
# arg1 trainingfile
# arg2 testfile
# arg3 attributefile (may be hardcoded instead)
import numpy as np
from sklearn.naive_bayes import GaussianNB
from operator import itemgetter, attrgetter, methodcaller
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
# trainingdata = np.array(trainingdata)
# trainingclasses = np.array(trainingclasses)
classAccuracyArray = [] #array of removed attrs along with their accuracy when removed
for x in range(0, len(trainingdata[0])):
    trainingdatacopy = np.empty_like(trainingdata)
    trainingdatacopy = trainingdata[:]
    for index, val in enumerate(trainingdatacopy):
        trainingdatacopy[index] = list(trainingdatacopy[index])
        del trainingdatacopy[index][x]
    trainingclassescopy = np.empty_like(trainingclasses)
    trainingclassescopy[:] = trainingclasses
    # load test data (testclasses not used)

    classifier = GaussianNB()
    classifier.fit(trainingdatacopy, trainingclassescopy)

    predictedVals = classifier.predict(trainingdatacopy)
    # what's my accuracy?
    acc = util.printAccuracy(predictedVals, trainingclassescopy)
    classAccuracyArray.append({"attributeindex":x, "accuracy":acc})

# now to build our actual learner after removing bad attributes classes
# find which attributes were least effective at predictions
sortedClassAccuracy = sorted(classAccuracyArray, key=itemgetter("accuracy"))
atrributesToRemove = []
for x in range(0, 10):
    y = -1 - x
    atrributesToRemove.append(sortedClassAccuracy[y]['attributeindex'])
atrributesToRemove = sorted(atrributesToRemove, reverse=True)
print("attr to remove ")
print(atrributesToRemove)
# remove them and then train
trainingdatacopy = np.empty_like(trainingdata)
trainingdatacopy = trainingdata[:]
for index, val in enumerate(trainingdatacopy):
    for removedClassIndex in atrributesToRemove:
        trainingdatacopy[index] = list(trainingdatacopy[index])
        del trainingdatacopy[index][removedClassIndex]
trainingclassescopy = np.empty_like(trainingclasses)
trainingclassescopy[:] = trainingclasses

classifier = GaussianNB()
classifier.fit(trainingdatacopy, trainingclassescopy)

predictedVals = classifier.predict(trainingdatacopy)
# what's my FINAL accuracy on the training data?
print("FINAL TRAINING ACCURACY")
acc = util.printAccuracy(predictedVals, trainingclassescopy)

# now classify test data and build prediction file
print("WRITING TEST PREDICTIONS TO FILE")
classifier = GaussianNB()
classifier.fit(trainingdatacopy, trainingclassescopy)
testclassescopy = np.empty_like(testclasses)
testclassescopy[:] = testclasses
predictedTestVals = classifier.predict(testclassescopy)
util.writePredictionsToFile(predictedTestVals)

