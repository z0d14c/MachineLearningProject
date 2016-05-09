# Util Function File
# tag130230

# read data from datafile
# filepath = string, filepath
# return (dataVals[], classVals[])
def readData(filepath):
    data = []
    classData = []
    f = open(filepath, 'r')
    fileLines = list(f)
    for line in fileLines:
        row = []
        for x in line.split():
            try: # for normal value
                row.append(float(x))
            except ValueError: # for missing value (? value)
                row.append(x)
        classVal = row[len(row)-1]
        classData.append(classVal)
        del row[-1]
        data.append(row)
    return data, classData

# read attrs from attr file
# attrFilePath = string, path to attribute listing file
def readAttributes(attrFilePath):
    attributes = []
    f = open(attrFilePath, 'r')
    fileLines = list(f)
    for line in fileLines:
        attr = line.split(":")[0]
        attributes.append(attr)
    return attributes

# write predictions to a file (for turning in)
def writePredictionsToFile(predictedvalues):
    predictionfile = open("prediction.txt", "w")
    for val in predictedvalues:
        predictionfile.write(str(int(val)) + "\n")

# print accuracy percentage
def printAccuracy(expectedValues, actualValues):
    correct = 0
    x = 0
    total = len(expectedValues)
    for val in expectedValues:
        if val == actualValues[x]:
            correct += 1
        x += 1
    print((correct / total) * 100)