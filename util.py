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

# # return data filtered by year, aka data[0]
# # data = array of arrays
# def filterByYear(data):
#